export async function onRequestGet(context) {
  const { GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET } = context.env;
  const url = new URL(context.request.url);
  const code = url.searchParams.get("code");

  if (!code) return new Response("No code provided", { status: 400 });

  const response = await fetch("https://github.com/login/oauth/access_token", {
    method: "POST",
    headers: {
      "content-type": "application/json",
      accept: "application/json",
      "user-agent": "cloudflare-pages-cms",
    },
    body: JSON.stringify({
      client_id: GITHUB_CLIENT_ID,
      client_secret: GITHUB_CLIENT_SECRET,
      code,
    }),
  });

  const result = await response.json();
  const token = result.access_token;
  const provider = "github";

  const script = `
    <script>
      (function() {
        function receiveMessage(e) {
          window.opener.postMessage(
            'authorization:${provider}:success:${JSON.stringify({ token: "${token}", provider: "${provider}" })}',
            e.origin
          );
        }
        window.addEventListener("message", receiveMessage, false);
        window.opener.postMessage("authorizing:${provider}", "*");
      })()
    </script>
  `;

  return new Response(script, {
    headers: { "content-type": "text/html;charset=UTF-8" },
  });
}