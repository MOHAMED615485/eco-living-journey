content = '''---
import BaseHead from '../components/BaseHead.astro';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
---

<html lang="en">
<head>
  <BaseHead
    title="Contact Ethan - Eco Living Journey"
    description="Have a question about solar generators or backup power? Contact Ethan directly at Eco Living Journey."
  />
  <style>
    :root {
      --green: #2d6a4f;
      --green-mid: #3d8b6f;
      --green-light: #a8d5b5;
      --green-pale: #d8f0e3;
      --cream: #f5f0dc;
      --cream-dark: #ede8d0;
      --text: #1a3d2b;
      --text-muted: #5a7a68;
      --orange: #e8790a;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: var(--cream); font-family: "DM Sans", sans-serif; color: var(--text); }

    .hero {
      background: var(--green);
      padding: 56px 24px;
      text-align: center;
      position: relative;
      overflow: hidden;
    }
    .hero::before {
      content: "";
      position: absolute;
      top: -60px; right: -60px;
      width: 220px; height: 220px;
      border-radius: 50%;
      background: rgba(168,213,181,0.1);
    }
    .hero h1 {
      font-family: "DM Serif Display", serif;
      font-size: clamp(28px,4vw,42px);
      color: white;
      margin-bottom: 12px;
      position: relative;
      z-index: 1;
    }
    .hero p {
      color: rgba(255,255,255,0.75);
      font-size: 16px;
      max-width: 480px;
      margin: 0 auto;
      line-height: 1.6;
      position: relative;
      z-index: 1;
    }

    .container {
      max-width: 760px;
      margin: 0 auto;
      padding: 56px 20px 80px;
    }

    .contact-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      margin-bottom: 40px;
    }

    .contact-card {
      background: white;
      border-radius: 20px;
      padding: 28px;
      box-shadow: 0 4px 24px rgba(45,106,79,0.10);
      border: 1px solid rgba(168,213,181,0.3);
      text-align: center;
    }

    .contact-card-icon {
      font-size: 40px;
      margin-bottom: 14px;
    }

    .contact-card h3 {
      font-family: "DM Serif Display", serif;
      font-size: 18px;
      color: var(--text);
      margin-bottom: 8px;
    }

    .contact-card p {
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.5;
      margin-bottom: 20px;
    }

    .btn-email {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 14px 24px;
      background: var(--green);
      color: white;
      border: none;
      border-radius: 50px;
      font-family: "DM Sans", sans-serif;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.2s;
      width: 100%;
      justify-content: center;
    }

    .btn-email:hover {
      background: var(--green-mid);
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(45,106,79,0.3);
    }

    .btn-amazon-contact {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 14px 24px;
      background: var(--orange);
      color: white;
      border: none;
      border-radius: 50px;
      font-family: "DM Sans", sans-serif;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.2s;
      width: 100%;
      justify-content: center;
    }

    .btn-amazon-contact:hover {
      background: #c96a08;
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(232,121,10,0.3);
    }

    .ethan-section {
      background: white;
      border-radius: 20px;
      padding: 32px;
      box-shadow: 0 4px 24px rgba(45,106,79,0.10);
      border: 1px solid rgba(168,213,181,0.3);
      display: flex;
      gap: 24px;
      align-items: flex-start;
      margin-bottom: 32px;
    }

    .ethan-avatar {
      width: 72px;
      height: 72px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--green) 0%, var(--green-mid) 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 32px;
      flex-shrink: 0;
    }

    .ethan-bio h2 {
      font-family: "DM Serif Display", serif;
      font-size: 22px;
      color: var(--text);
      margin-bottom: 8px;
    }

    .ethan-bio p {
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.65;
    }

    .faq-section h2 {
      font-family: "DM Serif Display", serif;
      font-size: 24px;
      color: var(--text);
      margin-bottom: 20px;
      text-align: center;
    }

    .faq-item {
      background: white;
      border-radius: 14px;
      padding: 20px 24px;
      margin-bottom: 12px;
      box-shadow: 0 2px 12px rgba(45,106,79,0.07);
      border: 1px solid rgba(168,213,181,0.3);
    }

    .faq-item h4 {
      font-size: 15px;
      font-weight: 700;
      color: var(--text);
      margin-bottom: 8px;
    }

    .faq-item p {
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.55;
    }

    .email-address {
      display: inline-block;
      background: var(--green-pale);
      color: var(--green);
      padding: 4px 12px;
      border-radius: 20px;
      font-weight: 700;
      font-size: 14px;
      margin: 4px 0;
    }

    @media (max-width: 580px) {
      .contact-grid { grid-template-columns: 1fr; }
      .ethan-section { flex-direction: column; }
    }
  </style>
</head>
<body>
  <Header />

  <div class="hero">
    <h1>Contact Ethan</h1>
    <p>Questions about solar generators, backup power, or my testing process? I read every email personally.</p>
  </div>

  <div class="container">

    <!-- ETHAN BIO -->
    <div class="ethan-section">
      <div class="ethan-avatar">E</div>
      <div class="ethan-bio">
        <h2>Hi, I am Ethan</h2>
        <p>
          I am a homeowner who lost $847 of food in a single blackout and spent 73 days testing solar generators to make sure it never happens again. I write honest reviews based on real watt readings, real surge tests, and real outage data. No paid partnerships, no sponsored reviews.
        </p>
        <p style="margin-top:10px;">
          Email me at <span class="email-address">ethan@ecoliving-journey.com</span>
        </p>
      </div>
    </div>

    <!-- CONTACT CARDS -->
    <div class="contact-grid">
      <div class="contact-card">
        <div class="contact-card-icon">✉️</div>
        <h3>General Questions</h3>
        <p>Ask me anything about solar generators, LRA ratings, surge requirements, or backup power setup.</p>
        <a
          href="mailto:ethan@ecoliving-journey.com?subject=Question%20from%20Eco%20Living%20Journey&body=Hi%20Ethan%2C%0A%0AI%20have%20a%20question%20about%20backup%20power%3A%0A%0A"
          class="btn-email"
        >
          ✉️ Email Ethan Directly
        </a>
      </div>

      <div class="contact-card">
        <div class="contact-card-icon">🛒</div>
        <h3>Product Questions</h3>
        <p>Not sure which generator fits your setup? Use the free sizing calculator or email me your appliance specs.</p>
        <a href="/solar-calculator/" class="btn-amazon-contact">
          ⚡ Use the Free Calculator
        </a>
      </div>

      <div class="contact-card">
        <div class="contact-card-icon">🤝</div>
        <h3>Partnership Inquiries</h3>
        <p>Brand partnerships and affiliate inquiries. I only partner with products I have personally tested.</p>
        <a
          href="mailto:ethan@ecoliving-journey.com?subject=Partnership%20Inquiry&body=Hi%20Ethan%2C%0A%0AI%20am%20reaching%20out%20regarding%20a%20potential%20partnership%3A%0A%0A"
          class="btn-email"
        >
          ✉️ Partnership Email
        </a>
      </div>

      <div class="contact-card">
        <div class="contact-card-icon">📰</div>
        <h3>Press and Media</h3>
        <p>Journalists and content creators looking to cite Eco Living Journey data or interview Ethan.</p>
        <a
          href="mailto:ethan@ecoliving-journey.com?subject=Press%20Inquiry&body=Hi%20Ethan%2C%0A%0AI%20am%20contacting%20you%20regarding%3A%0A%0A"
          class="btn-email"
        >
          ✉️ Press Email
        </a>
      </div>
    </div>

    <!-- FAQ -->
    <div class="faq-section">
      <h2>Common Questions</h2>

      <div class="faq-item">
        <h4>How quickly do you respond to emails?</h4>
        <p>Usually within 24-48 hours. I read every email personally and answer real questions about backup power setups.</p>
      </div>

      <div class="faq-item">
        <h4>Do you do custom sizing consultations?</h4>
        <p>Yes — email me your appliance list and LRA numbers and I will tell you exactly what you need. No charge.</p>
      </div>

      <div class="faq-item">
        <h4>Can I submit a product for review?</h4>
        <p>I only review products I can test for a minimum of 30 days on real appliances. Contact me with details and I will let you know if it fits my testing criteria.</p>
      </div>

      <div class="faq-item">
        <h4>Are your reviews sponsored?</h4>
        <p>No. I buy every product with my own money or purchase it before accepting any review unit. My recommendations are based on real test data only.</p>
      </div>
    </div>

  </div>

  <Footer />
</body>
</html>
'''

with open('src/pages/contact.astro', 'w', encoding='utf-8') as f:
    f.write(content)
print('done')
