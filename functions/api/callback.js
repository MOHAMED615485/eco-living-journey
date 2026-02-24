export async function onRequestGet(context) {
  // 1. GET THE CODE FROM THE URL (This was missing!)
  const { request, env } = context;
  const url = new URL(request.url);
  const code = url.searchParams.get("code");

  if (!code) {
    return new Response("No code found", { status: 400 });
  }

  // 2. EXCHANGE THE CODE FOR A TOKEN
  const response = await fetch("https://github.com/login/oauth/access_token", {
    method: "POST",
    headers: {
      "content-type": "application/json",
      accept: "application/json",
      "user-agent": "cloudflare-pages-cms",
    },
    body: JSON.stringify({
      client_id: env.GITHUB_CLIENT_ID,
      client_secret: env.GITHUB_CLIENT_SECRET,
      code,
    }),
  });

  const result = await response.json();
  const token = result.access_token;
  const provider = "github";

  // 3. RETURN THE TOKEN TO THE CMS
  const script = `
    <script>
      (function() {
        function receiveMessage(e) {
          console.log("Receive message:", e);
          window.opener.postMessage(
            'authorization:${provider}:success:${JSON.stringify({ token: token, provider: provider })}',
            e.origin
          );
        }
        window.addEventListener("message", receiveMessage, false);
        // Send a signal that we are ready
        window.opener.postMessage("authorizing:${provider}", "*");
      })()
    </script>
  `;

  return new Response(script, {
    headers: { "content-type": "text/html;charset=UTF-8" },
  });
}