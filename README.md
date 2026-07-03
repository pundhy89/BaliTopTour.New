<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bali Top Tour - Aplikasi Wisata Bali</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            line-height: 1.6;
        }
        
        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            text-align: center;
            color: white;
            padding: 40px 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        
        .header h1 {
            font-size: 3em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .header p {
            font-size: 1.2em;
            opacity: 0.95;
        }
        
        .emoji {
            font-size: 1.2em;
            margin-right: 8px;
        }
        
        .section {
            background: white;
            border-radius: 12px;
            padding: 30px;
            margin-bottom: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            border-left: 5px solid #667eea;
        }
        
        .section h2 {
            color: #667eea;
            font-size: 1.8em;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
        }
        
        .section h3 {
            color: #764ba2;
            font-size: 1.2em;
            margin-top: 20px;
            margin-bottom: 15px;
        }
        
        .download-btn {
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 40px;
            border-radius: 50px;
            text-decoration: none;
            font-size: 1.1em;
            font-weight: bold;
            margin: 15px 0;
            transition: transform 0.3s, box-shadow 0.3s;
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        
        .download-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
        }
        
        .info-box {
            background: #f8f9ff;
            border-left: 4px solid #667eea;
            padding: 20px;
            border-radius: 8px;
            margin: 15px 0;
        }
        
        .steps {
            list-style: none;
            counter-reset: step-counter;
        }
        
        .steps li {
            counter-increment: step-counter;
            padding: 15px 20px;
            margin: 10px 0;
            background: #f8f9ff;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }
        
        .steps li::before {
            content: counter(step-counter);
            display: inline-block;
            background: #667eea;
            color: white;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            text-align: center;
            line-height: 30px;
            margin-right: 15px;
            font-weight: bold;
        }
        
        .links {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }
        
        .link-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-decoration: none;
            transition: transform 0.3s;
            text-align: center;
        }
        
        .link-card:hover {
            transform: translateY(-5px);
        }
        
        .link-card h4 {
            margin-bottom: 10px;
            font-size: 1.1em;
        }
        
        .code-block {
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 15px;
            border-radius: 8px;
            overflow-x: auto;
            margin: 15px 0;
            font-family: 'Courier New', monospace;
        }
        
        .version-badge {
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            margin-left: 10px;
        }
        
        .footer {
            text-align: center;
            color: white;
            padding: 20px;
            margin-top: 40px;
            font-size: 0.95em;
        }
        
        .tech-stack {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 10px;
            margin: 15px 0;
        }
        
        .tech-item {
            background: #f0f0f0;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            border: 2px solid #667eea;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <div class="header">
            <h1><span class="emoji">🌴</span>Bali Top Tour</h1>
            <p>Aplikasi Wisata Pintar untuk Menemukan Destinasi Terbaik di Bali</p>
        </div>
        
        <!-- Download Section -->
        <div class="section">
            <h2><span class="emoji">📥</span>Download Aplikasi</h2>
            <div class="info-box">
                <strong>Versi Terbaru: v1.0.0</strong><br>
                Unduh aplikasi Bali Top Tour langsung ke perangkat Android Anda.
            </div>
            <a href="https://github.com/pundhy89/BaliTopTour.New/releases/download/v1.0.0/BaliTopTour.v3.apk" class="download-btn">
                <span class="emoji">⬇️</span> Download APK v1.0.0
            </a>
            
            <h3>📱 Cara Instalasi</h3>
            <ol class="steps">
                <li><strong>Download</strong> file APK dari tombol di atas</li>
                <li><strong>Aktifkan</strong> "Install dari sumber tidak dikenal" di Pengaturan → Keamanan</li>
                <li><strong>Buka</strong> file APK yang sudah diunduh</li>
                <li><strong>Ikuti</strong> proses instalasi</li>
                <li><strong>Selesai!</strong> Nikmati aplikasi Bali Top Tour</li>
            </ol>
        </div>
        
        <!-- Quick Links -->
        <div class="section">
            <h2><span class="emoji">🔗</span>Link Penting</h2>
            <div class="links">
                <a href="https://balitoptour-new.vercel.app" class="link-card">
                    <h4>🌐 Website Live</h4>
                    <p>Kunjungi aplikasi web</p>
                </a>
                <a href="https://aistudio.google.com" class="link-card">
                    <h4>✨ AI Studio</h4>
                    <p>Powered by Gemini AI</p>
                </a>
                <a href="https://github.com/pundhy89/BaliTopTour.New/releases" class="link-card">
                    <h4>📦 Releases</h4>
                    <p>Lihat semua versi</p>
                </a>
            </div>
        </div>
        
        <!-- Development Section -->
        <div class="section">
            <h2><span class="emoji">💻</span>Untuk Developer</h2>
            
            <h3>📋 Prerequisites</h3>
            <p>Node.js dan npm harus terinstall di komputer Anda.</p>
            
            <h3>🚀 Setup Lokal</h3>
            <ol class="steps">
                <li><strong>Clone</strong> repository ini</li>
                <li><strong>Install</strong> dependencies dengan menjalankan:
                    <div class="code-block">npm install</div>
                </li>
                <li><strong>Set API Key</strong> di file <code>.env.local</code>:
                    <div class="code-block">GEMINI_API_KEY=your_api_key_here</div>
                </li>
                <li><strong>Jalankan</strong> aplikasi:
                    <div class="code-block">npm run dev</div>
                </li>
                <li><strong>Buka</strong> browser dan akses <code>http://localhost:3000</code></li>
            </ol>
            
            <h3>🛠️ Tech Stack</h3>
            <div class="tech-stack">
                <div class="tech-item">TypeScript</div>
                <div class="tech-item">React</div>
                <div class="tech-item">Next.js</div>
                <div class="tech-item">Gemini AI</div>
                <div class="tech-item">Vercel</div>
            </div>
        </div>
        
        <!-- Footer -->
        <div class="footer">
            <p>💜 Dibuat dengan cinta oleh <strong><a href="https://github.com/pundhy89" style="color: white; text-decoration: underline;">pundhy89</a></strong></p>
            <p style="margin-top: 10px; opacity: 0.8;">© 2026 Bali Top Tour. Semua hak dilindungi.</p>
        </div>
    </div>
</body>
</html>
