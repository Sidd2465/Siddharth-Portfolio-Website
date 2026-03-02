import streamlit as st
import base64

def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# Page Config
st.set_page_config(
    page_title="Siddharth's Portfolio",
    page_icon="💼",
    layout="wide"
)

# ─── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&family=Poppins:wght@300;400;600;700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        background-image: url('https://static.vecteezy.com/system/resources/previews/013/684/168/non_2x/abstract-neon-lights-dots-particles-dynamic-wave-flowing-on-dark-background-technology-digital-futuristic-concept-vector.jpg');
        background-size: cover;
        background-attachment: fixed;
        color: #e0e0e0;
        font-family: 'Poppins', sans-serif;
    }
    .particles { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; }
    .particle { position: absolute; background: #FF6B6B; border-radius: 50%; opacity: 0.6; animation: float 15s infinite linear; }
    @keyframes float {
        0% { transform: translateY(100vh) translateX(0); opacity: 0; }
        10% { opacity: 0.6; } 90% { opacity: 0.6; }
        100% { transform: translateY(-100px) translateX(100px); opacity: 0; }
    }
    .gradient-text {
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4, #45B7D1);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
        font-weight: 700; font-family: 'Orbitron', sans-serif;
    }
    .glass-card {
        background: rgba(22, 33, 62, 0.4); backdrop-filter: blur(10px);
        border-radius: 20px; border: 1px solid rgba(255, 107, 107, 0.3);
        padding: 25px; box-shadow: 0 8px 32px rgba(0,0,0,0.4); transition: all 0.4s ease;
    }
    .glass-card:hover { transform: translateY(-10px); box-shadow: 0 20px 50px rgba(255,107,107,0.4); border-color: #FF6B6B; }
    .stButton>button {
        background: rgba(255,107,107,0.1); border: 2px solid #FF6B6B; color: white;
        border-radius: 15px; padding: 10px 20px; font-weight: 600; transition: all 0.4s ease;
    }
    .stButton>button:hover { background: #FF6B6B; box-shadow: 0 0 20px rgba(255,107,107,0.8); transform: scale(1.05); }
    .profile-img { border: 6px solid #FF6B6B; box-shadow: 0 0 60px rgba(255,107,107,0.8); animation: floatProfile 6s ease-in-out infinite; }
    @keyframes floatProfile { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-20px); } }
    .stat-card, .skill-card {
        background: rgba(22,33,62,0.5); backdrop-filter: blur(8px);
        border-radius: 15px; padding: 20px; text-align: center;
        border: 1px solid rgba(255,107,107,0.3); transition: all 0.4s ease;
    }
    .stat-card:hover, .skill-card:hover { transform: translateY(-10px) scale(1.03); box-shadow: 0 15px 40px rgba(255,107,107,0.5); border-color: #FF6B6B; }
    .progress-bar { background: linear-gradient(90deg, #FF6B6B, #4ECDC4); box-shadow: 0 0 15px rgba(255,107,107,0.8); height: 8px; border-radius: 10px; }
    .social-card:hover { transform: translateY(-10px) rotate(8deg) scale(1.1); box-shadow: 0 20px 40px rgba(0,0,0,0.5); }
    hr { border: none; height: 3px; background: linear-gradient(90deg, transparent, #FF6B6B, transparent); margin: 50px 0; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; }

    /* Chat / Voice Assistant */
    .voice-assistant-btn {
        position: fixed; bottom: 30px; right: 30px; width: 70px; height: 70px; border-radius: 50%;
        background: linear-gradient(135deg, #FF6B6B, #FF8E53); border: 3px solid rgba(255,107,107,0.5);
        box-shadow: 0 0 30px rgba(255,107,107,0.6); cursor: pointer; display: flex;
        align-items: center; justify-content: center; font-size: 2em; z-index: 1000; transition: all 0.3s ease; animation: pulse 2s infinite;
    }
    .voice-assistant-btn:hover { transform: scale(1.1); box-shadow: 0 0 50px rgba(255,107,107,0.9); }
    @keyframes pulse { 0%,100% { box-shadow: 0 0 30px rgba(255,107,107,0.6); } 50% { box-shadow: 0 0 50px rgba(255,107,107,0.9); } }
    @keyframes listening-pulse { 0%,100% { transform: scale(1); } 50% { transform: scale(1.15); } }
    .chat-window {
        position: fixed; bottom: 120px; right: 30px; width: 420px; height: 600px;
        background: rgba(22,33,62,0.98); backdrop-filter: blur(20px); border-radius: 25px;
        border: 2px solid rgba(255,107,107,0.4); box-shadow: 0 15px 50px rgba(0,0,0,0.6);
        z-index: 999; display: flex; flex-direction: column; overflow: hidden; animation: slideUp 0.3s ease-out;
    }
    @keyframes slideUp { from { transform: translateY(20px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
    .chat-header { background: linear-gradient(135deg, #FF6B6B, #FF8E53); padding: 20px; display: flex; justify-content: space-between; align-items: center; }
    .chat-header h3 { margin: 0; color: white; font-size: 1.3em; }
    .close-chat { background: rgba(255,255,255,0.2); border: none; color: white; width: 30px; height: 30px; border-radius: 50%; cursor: pointer; font-size: 1.2em; transition: all 0.3s ease; }
    .close-chat:hover { background: rgba(255,255,255,0.3); transform: rotate(90deg); }
    .chat-messages { flex: 1; overflow-y: auto; padding: 20px; display: flex; flex-direction: column; gap: 15px; }
    .chat-messages::-webkit-scrollbar { width: 8px; }
    .chat-messages::-webkit-scrollbar-thumb { background: linear-gradient(135deg, #FF6B6B, #FF8E53); border-radius: 10px; }
    .message { display: flex; flex-direction: column; max-width: 80%; animation: messageSlide 0.3s ease-out; }
    @keyframes messageSlide { from { transform: translateY(10px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
    .message.user { align-self: flex-end; }
    .message.assistant { align-self: flex-start; }
    .message-bubble { padding: 12px 16px; border-radius: 18px; word-wrap: break-word; line-height: 1.5; }
    .message.user .message-bubble { background: linear-gradient(135deg, #4ECDC4, #45B7D1); color: white; border-bottom-right-radius: 4px; }
    .message.assistant .message-bubble { background: rgba(255,107,107,0.15); color: #e0e0e0; border: 1px solid rgba(255,107,107,0.3); border-bottom-left-radius: 4px; }
    .message-time { font-size: 0.7em; color: #888; margin-top: 4px; padding: 0 8px; }
    .typing-indicator { display: flex; gap: 4px; padding: 12px 16px; background: rgba(255,107,107,0.15); border: 1px solid rgba(255,107,107,0.3); border-radius: 18px; width: fit-content; }
    .typing-dot { width: 8px; height: 8px; border-radius: 50%; background: #FF6B6B; animation: typingDot 1.4s infinite; }
    .typing-dot:nth-child(2) { animation-delay: 0.2s; } .typing-dot:nth-child(3) { animation-delay: 0.4s; }
    @keyframes typingDot { 0%,60%,100% { transform: translateY(0); opacity: 0.7; } 30% { transform: translateY(-10px); opacity: 1; } }
    .chat-input-area { padding: 15px 20px; background: rgba(15,20,35,0.8); border-top: 1px solid rgba(255,107,107,0.2); display: flex; gap: 10px; align-items: center; }
    .chat-input { flex: 1; background: rgba(255,255,255,0.05); border: 2px solid rgba(255,107,107,0.3); border-radius: 25px; padding: 12px 18px; color: white; font-size: 0.95em; outline: none; transition: all 0.3s ease; }
    .chat-input:focus { border-color: #FF6B6B; background: rgba(255,255,255,0.08); box-shadow: 0 0 15px rgba(255,107,107,0.3); }
    .chat-input::placeholder { color: #888; }
    .voice-input-btn, .send-btn { width: 45px; height: 45px; border-radius: 50%; border: none; cursor: pointer; font-size: 1.3em; transition: all 0.3s ease; display: flex; align-items: center; justify-content: center; }
    .voice-input-btn { background: linear-gradient(135deg, #4ECDC4, #45B7D1); box-shadow: 0 4px 15px rgba(78,205,196,0.4); }
    .voice-input-btn:hover { transform: scale(1.1); }
    .send-btn { background: linear-gradient(135deg, #FF6B6B, #FF8E53); box-shadow: 0 4px 15px rgba(255,107,107,0.4); }
    .send-btn:hover { transform: scale(1.1); }
    .welcome-message { background: rgba(78,205,196,0.1); border: 1px solid rgba(78,205,196,0.3); border-radius: 15px; padding: 15px; margin-bottom: 10px; }
    .welcome-message h4 { color: #4ECDC4; margin: 0 0 10px 0; }
    .quick-command { background: rgba(255,107,107,0.1); border: 1px solid rgba(255,107,107,0.2); padding: 8px 12px; border-radius: 20px; margin: 5px; display: inline-block; font-size: 0.85em; color: #FF6B6B; cursor: pointer; transition: all 0.3s ease; }
    .quick-command:hover { background: rgba(255,107,107,0.2); transform: translateY(-2px); }
    </style>
""", unsafe_allow_html=True)

# Floating particles
particle_html = "<div class='particles'>"
for i in range(30):
    size = 4 + (i % 10)
    left = (i * 137) % 100
    delay = i * 0.5
    duration = 10 + (i % 10)
    color = "#FF6B6B" if i % 2 == 0 else "#4ECDC4"
    particle_html += f"<div class='particle' style='width:{size}px;height:{size}px;left:{left}%;animation-delay:{delay}s;animation-duration:{duration}s;background:{color};'></div>"
particle_html += "</div>"
st.markdown(particle_html, unsafe_allow_html=True)

# Session state
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# ─── NAVIGATION ───────────────────────────────────────────────────────────────
st.markdown("<div style='position: relative; z-index: 10;'>", unsafe_allow_html=True)
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([1.5, 1, 1, 1, 1, 1, 1.3, 1.2])
with col1:
    st.markdown('<h3 class="gradient-text">Siddharth Singhal</h3>', unsafe_allow_html=True)

nav_pages = ["Home", "About", "Projects", "Hackathons", "Contact", "Resume"]
nav_icons = ["🏠", "👤", "💼", "🏆", "📬", "📄"]
nav_cols = [col2, col3, col4, col5, col6, col7]
for page, icon, col in zip(nav_pages, nav_icons, nav_cols):
    with col:
        if st.button(f"{icon} {page}", key=f"nav_{page}"):
            st.session_state.page = page

st.markdown("---")
st.markdown("</div>", unsafe_allow_html=True)

# ─── VOICE ASSISTANT ──────────────────────────────────────────────────────────
voice_assistant_html = """
<div id="chatWindow" class="chat-window" style="display: none;">
    <div class="chat-header">
        <h3>🤖 AI Assistant</h3>
        <button class="close-chat" onclick="toggleChat()">✕</button>
    </div>
    <div class="chat-messages" id="chatMessages">
        <div class="welcome-message">
            <h4>👋 Hello! I'm your AI assistant</h4>
            <p style="color:#e0e0e0;font-size:0.9em;margin:5px 0;">Ask me anything about Siddharth:</p>
            <div style="margin-top:10px;">
                <span class="quick-command" onclick="sendQuickCommand('Tell me about yourself')">👋 About</span>
                <span class="quick-command" onclick="sendQuickCommand('What are your skills?')">💼 Skills</span>
                <span class="quick-command" onclick="sendQuickCommand('Go to projects')">🚀 Projects</span>
                <span class="quick-command" onclick="sendQuickCommand('What hackathons have you won?')">🏆 Hackathons</span>
            </div>
        </div>
    </div>
    <div class="chat-input-area">
        <button class="voice-input-btn" id="voiceInputBtn" onclick="toggleVoiceInput()" title="Voice Input">🎤</button>
        <input type="text" class="chat-input" id="chatInput" placeholder="Type a message or use voice..."
               onkeypress="if(event.key==='Enter') sendMessage()">
        <button class="send-btn" onclick="sendMessage()" title="Send">➤</button>
    </div>
</div>
<div id="voiceBtn" class="voice-assistant-btn" onclick="toggleChat()">💬</div>
<script>
(function() {
    let recognition, isListening = false;
    let synth = window.speechSynthesis;

    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
        const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
        recognition = new SR();
        recognition.continuous = false; recognition.interimResults = false; recognition.lang = 'en-US';
        recognition.onresult = e => { const i = document.getElementById('chatInput'); if(i){i.value=e.results[0][0].transcript; sendMessage();} };
        recognition.onerror = () => stopVoice();
        recognition.onend = () => stopVoice();
    }

    window.toggleChat = function() {
        const w = document.getElementById('chatWindow'), b = document.getElementById('voiceBtn');
        if (!w||!b) return;
        if (w.style.display==='none'||w.style.display==='') {
            w.style.display='flex'; b.innerHTML='✕'; b.style.background='linear-gradient(135deg,#4ECDC4,#45B7D1)';
        } else {
            w.style.display='none'; b.innerHTML='💬'; b.style.background='linear-gradient(135deg,#FF6B6B,#FF8E53)'; stopVoice();
        }
    };

    window.toggleVoiceInput = function() { isListening ? stopVoice() : startVoice(); };

    function startVoice() {
        if (recognition&&!isListening) {
            const b = document.getElementById('voiceInputBtn');
            if(b){b.classList.add('active');b.innerHTML='🎙️';}
            isListening=true; try{recognition.start();}catch(e){stopVoice();}
        }
    }
    function stopVoice() {
        if (recognition&&isListening) {
            const b = document.getElementById('voiceInputBtn');
            if(b){b.classList.remove('active');b.innerHTML='🎤';}
            isListening=false; try{recognition.stop();}catch(e){}
        }
    }

    window.sendQuickCommand = function(cmd) { const i=document.getElementById('chatInput'); if(i){i.value=cmd;sendMessage();} };

    window.sendMessage = function() {
        const i=document.getElementById('chatInput'); if(!i) return;
        const msg=i.value.trim(); if(!msg) return;
        addMsg(msg,'user'); i.value=''; showTyping();
        setTimeout(() => {
            hideTyping();
            const r=respond(msg.toLowerCase());
            addMsg(r.text,'assistant'); speak(r.text);
            if(r.nav) setTimeout(() => { document.querySelectorAll('button').forEach(b=>{if(b.textContent.includes(r.nav))b.click();}); }, 1500);
        }, 1000);
    };

    function addMsg(text,sender) {
        const d=document.getElementById('chatMessages'); if(!d) return;
        const el=document.createElement('div'); el.className='message '+sender;
        const n=new Date(), t=n.getHours().toString().padStart(2,'0')+':'+n.getMinutes().toString().padStart(2,'0');
        el.innerHTML=`<div class="message-bubble">${text}</div><div class="message-time">${t}</div>`;
        d.appendChild(el); d.scrollTop=d.scrollHeight;
    }

    function showTyping() {
        const d=document.getElementById('chatMessages'); if(!d) return;
        const el=document.createElement('div'); el.id='typingIndicator'; el.className='message assistant';
        el.innerHTML='<div class="typing-indicator"><div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div></div>';
        d.appendChild(el); d.scrollTop=d.scrollHeight;
    }
    function hideTyping() { const el=document.getElementById('typingIndicator'); if(el)el.remove(); }

    function speak(text) {
        if(synth.speaking)synth.cancel();
        const u=new SpeechSynthesisUtterance(text); u.rate=1.0; u.pitch=1.0; u.volume=1.0; synth.speak(u);
    }

    function respond(c) {
        let r={text:'',nav:null};
        if(c.includes('home')){r.nav='Home';r.text='Taking you home! 🏠';}
        else if(c.includes('about')&&!c.includes('yourself')&&!c.includes('who')){r.nav='About';r.text='Opening the About page! 👤';}
        else if(c.includes('project')){r.nav='Projects';r.text="Let me show you Siddharth's projects — EcoSentinel, Sudarshan AI, and more! 💼";}
        else if(c.includes('hackathon')||c.includes('award')||c.includes('competition')){r.nav='Hackathons';r.text='Navigating to Hackathons & Awards! 🏆';}
        else if(c.includes('contact')){r.nav='Contact';r.text='Going to the contact page! 📬';}
        else if(c.includes('resume')||c.includes('cv')){r.nav='Resume';r.text='Opening the Resume page! 📄';}
        else if(c.includes('yourself')||c.includes('who are you')||c.includes('introduce')){r.text="Hi! I'm Siddharth Singhal — an Electronics & AI Engineer from Thapar Institute. I specialise in Embedded Systems, AI/ML, and Computer Vision. I interned at Siemens Healthineers and won the Innovation Award at AI for Sustainability Hackathon 2026! 🚀";}
        else if(c.includes('skill')||c.includes('technolog')){r.text="I'm proficient in Embedded C, C++, Python, and MATLAB. I work with Arduino, ESP32, STM32, and Raspberry Pi. My AI stack includes TensorFlow, OpenCV, and Scikit-learn. I know I2C, SPI, and CAN protocols! 💻";}
        else if(c.includes('email')||c.includes('contact info')||c.includes('reach')){r.text="Reach me at siddharthsinghal2465@gmail.com or +91-9815315327. Always happy to connect! 📧";}
        else if(c.includes('education')||c.includes('college')||c.includes('study')){r.text="I'm pursuing B.E. in Electronics, Instrumentation and Control Engineering at Thapar Institute (TIET), Patiala. CGPA: 7.28/10, graduating 2027! 🎓";}
        else if(c.includes('ecosentinel')||c.includes('boat')||c.includes('water quality')){r.text="EcoSentinel is my autonomous water-surface vehicle for real-time water quality monitoring! It integrates pH, turbidity, temperature, and DO sensors. It won the Innovation Award at AI for Sustainability Hackathon 2026! 🚤";}
        else if(c.includes('sudarshan')||c.includes('legal')||c.includes('document')){r.text="Sudarshan AI is my smart legal document summarizer! It uses LLMs to extract key clauses and summaries from complex legal documents, making them accessible to everyone. 📜";}
        else if(c.includes('gesture')||c.includes('glove')){r.text="My Hand Gesture Glove uses flex sensors on an ESP32 to detect gestures in real time. I also built a companion web app that recognises gestures via both the glove and a live camera using OpenCV! 🖐️";}
        else if(c.includes('siemens')||c.includes('intern')){r.text="I interned at Siemens Healthineers in Bangalore, building a DICOM Image Resizer and Viewer. I implemented Bilinear, Bicubic, and Lanczos interpolation and evaluated quality using PSNR and SSIM! 🏥";}
        else if(c.includes('open source')||c.includes('gssoc')||c.includes('osci')){r.text="I contributed to open source via GirlScript Summer of Code 2025 (GSSoC) and Open Source Connect India 2025 (OSCI) — bug fixes, features, and documentation across multiple repos! 🌍";}
        else if(c.includes('sih')||c.includes('smart india')){r.text="I participated in Smart India Hackathon 2025, building a Smart Track Recording Car — an embedded vehicle that maps vehicle paths in real time using sensor fusion! 🚂";}
        else if(c.includes('sustainab')||c.includes('stormbreakers')||c.includes('innovation')){r.text="Team Stormbreakers won the Innovation Award at AI for Sustainability Hackathon 2026 (Canadian University Dubai)! We presented EcoSentinel, our autonomous water-quality monitoring boat. 🏆";}
        else if(c.includes('hello')||c.includes('hi ')||c.includes('hey')){r.text="Hello! 👋 Ask me about Siddharth's skills, projects, hackathons, or experience!";}
        else if(c.includes('thank')){r.text="You're welcome! 😊 Anything else?";}
        else{r.text="Try asking me about projects like EcoSentinel or Sudarshan AI, hackathons, internship at Siemens, or open source contributions! 🤔";}
        return r;
    }
})();
</script>
"""
st.markdown(voice_assistant_html, unsafe_allow_html=True)


# ══════════════════════════════════════════════
# HOME PAGE
# ══════════════════════════════════════════════
if st.session_state.page == 'Home':
    col_text, col_image = st.columns([1, 1], gap="large")

    with col_text:
        st.markdown('<h1 style="font-size:4em;">Welcome to My</h1>', unsafe_allow_html=True)
        st.markdown('<h1 class="gradient-text" style="font-size:4em;">Portfolio Website</h1>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:1.5em;color:#4ECDC4;">Electronics & AI Engineer | Embedded Systems | Open Source Contributor</p>', unsafe_allow_html=True)
        st.write("""
        Hi! I'm **Siddharth Singhal**, a Pre Final Year Electronics Instrumentation and Control Engineering student at Thapar Institute of Engineering and Technology, Patiala. I am  Highly passionate about Electronics and AI, and  specialising in **Embedded Systems, AI/ML, 
        and Computer Vision**.Love to work on innovative projects that solve real world problems.  
        🏆 **Innovation Award** winner at AI for Sustainability Hackathon 2026 — Team Stormbreakers.
        """)
        st.markdown("""
            <div style="margin:30px 0;">
                <span style="background:linear-gradient(135deg,#FF6B6B,#FF8E53);padding:10px 20px;border-radius:30px;margin:8px;display:inline-block;box-shadow:0 0 15px rgba(255,107,107,0.5);">Python</span>
                <span style="background:linear-gradient(135deg,#4ECDC4,#45B7D1);padding:10px 20px;border-radius:30px;margin:8px;display:inline-block;box-shadow:0 0 15px rgba(78,205,196,0.5);">Embedded C/C++</span>
                <span style="background:linear-gradient(135deg,#A8E6CF,#88D8B0);padding:10px 20px;border-radius:30px;margin:8px;display:inline-block;">AI/ML</span>
                <span style="background:linear-gradient(135deg,#FFD93D,#FFA93D);padding:10px 20px;border-radius:30px;margin:8px;display:inline-block;">IoT</span>
                <span style="background:linear-gradient(135deg,#C77DFF,#9B59B6);padding:10px 20px;border-radius:30px;margin:8px;display:inline-block;">Open Source</span>
            </div>
        """, unsafe_allow_html=True)
        bc1, bc2 = st.columns(2)
        with bc1:
            if st.button("🚀 Explore About Me", key="btn_about"):
                st.session_state.page = 'About'
        with bc2:
            if st.button("📥 Download Resume", key="btn_resume"):
                st.session_state.page = 'Resume'

    with col_image:
        img_b64 = get_image_base64("sidimage.jpeg")
        if img_b64:
            st.markdown(f'<div style="display:flex;justify-content:center;margin-top:50px;"><img src="data:image/jpeg;base64,{img_b64}" class="profile-img" style="border-radius:50%;width:400px;height:400px;object-fit:cover;"></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div style="display:flex;justify-content:center;margin-top:50px;"><div style="width:400px;height:400px;border-radius:50%;background:linear-gradient(135deg,#FF6B6B,#4ECDC4);box-shadow:0 0 80px rgba(255,107,107,0.8);display:flex;align-items:center;justify-content:center;color:white;font-size:4em;">SS</div></div>', unsafe_allow_html=True)

    # Award strip
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
        <div style="background:linear-gradient(135deg,rgba(255,217,61,0.15),rgba(255,169,61,0.1));
                    border:1px solid rgba(255,217,61,0.4);border-radius:20px;padding:20px;text-align:center;">
            <h3 style="color:#FFD93D;margin:0 0 10px 0;">🏆 Latest Achievement</h3>
            <p style="font-size:1.1em;color:#e0e0e0;margin:0;">
                Won the <strong style="color:#FFD93D;">Innovation Award</strong> at
                <strong>AI for Sustainability Hackathon 2026</strong> (Canadian University Dubai, UAE) —
                Team <strong>Stormbreakers</strong> | Feb 14–16, 2026
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Quick stats
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown('<h2 class="gradient-text" style="text-align:center;font-size:3em;">Quick Stats</h2>', unsafe_allow_html=True)
    sc1, sc2, sc3, sc4, sc5 = st.columns(5)
    for col, val, label, color in [
        (sc1, "2+", "Years Experience", "#FF6B6B"),
        (sc2, "10+", "Projects Built", "#4ECDC4"),
        (sc3, "3", "Hackathons", "#45B7D1"),
        (sc4, "🏆 1", "Innovation Award", "#FFD93D"),
        (sc5, "2", "Open Source\nProgrammes", "#C77DFF"),
    ]:
        with col:
            st.markdown(f'<div class="stat-card glass-card"><h1 style="color:{color};font-size:3em;margin:0;">{val}</h1><p style="font-size:0.95em;margin:10px 0;">{label}</p></div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════
# ABOUT PAGE
# ══════════════════════════════════════════════
elif st.session_state.page == 'About':
    st.markdown('<h1 class="gradient-text" style="font-size:3em;">About Me</h1>', unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    col_l, col_r = st.columns([2, 1], gap="large")

    with col_l:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h3 style="color:#4ECDC4;">Who I Am</h3>', unsafe_allow_html=True)
        st.write("""
        I'm **Siddharth Singhal**, a passionate Electronics and Instrumentation Engineering student at 
        **Thapar Institute of Engineering and Technology** focused on **Embedded Systems, AI/ML, and Computer Vision**.

        I have industry experience as a **Software Intern at Siemens Healthineers** (Bangalore), where I built a 
        DICOM Image Resizer and Viewer for medical imaging systems. Previously, I interned at 
        **Punjab Engineering College**, working on semiconductor fabrication and FPGA programming.

        I am an active **open-source contributor** via **GirlScript Summer of Code 2025 (GSSoC)** and 
        **Open Source Connect India 2025 (OSCI)**. I am a proud **Innovation Award winner** at the 
        AI for Sustainability Hackathon 2026 (Canadian University Dubai), a **SIH 2025** participant 
        (Smart Track Recording Car), and an **Agentic AI Hackathon 2025** participant (Ulster University, UK).

        I believe in building solutions that create real-world impact — from autonomous water-quality 
        monitoring boats to AI-powered legal document summarizers.
        """)

        st.markdown('<h3 style="color:#4ECDC4;margin-top:30px;">Technical Expertise</h3>', unsafe_allow_html=True)
        for sname, stech, prog in [
            ("🔌 Embedded Systems & Hardware", "Arduino, ESP32, STM32, Raspberry Pi, I2C, SPI, CAN", 90),
            ("🤖 AI/ML & Computer Vision", "TensorFlow, OpenCV, Scikit-learn, NumPy, Pandas", 82),
            ("💻 Programming Languages", "Embedded C, C++, Python, MATLAB, Verilog, Assembly, R", 88),
            ("🛠️ EDA & Simulation Tools", "Cadence Virtuoso, HFSS ANSYS, MATLAB/Simulink, LabVIEW", 78),
            ("🌐 Web & Dashboard Development", "Streamlit, Flask, Python Dashboards", 75),
            ("🗂️ Dev Practices", "Git, SDLC, OOP, DSA, Modular Firmware Design", 85),
        ]:
            st.markdown(f"""
                <div class="skill-card glass-card" style="margin-bottom:12px;">
                    <h4 style="margin:0 0 8px 0;color:#FF6B6B;">{sname}</h4>
                    <p style="margin:0 0 8px 0;color:#cccccc;">{stech}</p>
                    <div style="background:rgba(255,255,255,0.1);border-radius:10px;height:8px;overflow:hidden;">
                        <div class="progress-bar" style="width:{prog}%;"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_r:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h3 style="color:#4ECDC4;">Highlights</h3>', unsafe_allow_html=True)
        for val, label, color in [
            ("🏆 1", "Innovation Award", "#FFD93D"),
            ("3", "Hackathons", "#FF6B6B"),
            ("2", "Open Source Programmes", "#4ECDC4"),
            ("7.28", "CGPA at TIET", "#45B7D1"),
            ("2", "Internships", "#C77DFF"),
        ]:
            st.markdown(f'<div class="stat-card" style="margin-bottom:15px;"><h1 style="color:{color};margin:0;font-size:2.2em;">{val}</h1><p style="margin:8px 0 0 0;font-size:0.95em;">{label}</p></div>', unsafe_allow_html=True)

        st.markdown('<h3 style="color:#4ECDC4;margin-top:20px;">Open Source</h3>', unsafe_allow_html=True)
        st.markdown("""
            <div style="background:rgba(199,125,255,0.1);border:1px solid rgba(199,125,255,0.3);border-radius:15px;padding:15px;margin-bottom:12px;">
                <p style="color:#C77DFF;font-weight:700;margin:0 0 5px 0;">GSSoC 2025</p>
                <p style="color:#cccccc;font-size:0.85em;margin:0;">GirlScript Summer of Code</p>
            </div>
            <div style="background:rgba(78,205,196,0.1);border:1px solid rgba(78,205,196,0.3);border-radius:15px;padding:15px;">
                <p style="color:#4ECDC4;font-weight:700;margin:0 0 5px 0;">OSCI 2025</p>
                <p style="color:#cccccc;font-size:0.85em;margin:0;">Open Source Connect India</p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════
# PROJECTS PAGE
# ══════════════════════════════════════════════
elif st.session_state.page == 'Projects':
    st.markdown('<h1 class="gradient-text" style="font-size:3em;">My Projects</h1>', unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    tab_sw, tab_hw = st.tabs(["🤖 AI & Software Projects", "⚙️ Hardware & Embedded Systems"])

    # ── SOFTWARE ──────────────────────────────
    with tab_sw:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### AI / Software Projects")

        # Sudarshan AI
        with st.expander("⚖️ Sudarshan AI — Smart Legal Document Summarizer", expanded=True):
            c1, c2 = st.columns([2, 1])
            with c1:
                st.markdown("**Stack:** Python · LLM APIs · NLP · Streamlit")
                st.write("""
                AI-powered web app for summarising and analysing complex legal documents. 
                Users upload contracts or court documents and instantly receive plain-language 
                summaries of key clauses, obligations, and deadlines via an LLM pipeline.

                **Key Features:**
                - LLM-based extraction of important clauses and obligations
                - Plain-language summaries for non-technical users
                - Interactive Q&A interface for querying document content
                - Clean Streamlit interface
                """)
                if st.button("View on GitHub", key="g_sudarshan"):
                    st.write("🔗 [GitHub](https://github.com/Sidd2465/Sudarnshan-AI)")
            with c2:
                st.markdown("**Status:** ✅ Completed")
                st.markdown("- 📜 LLM-Powered NLP")
                st.markdown("- ⚡ Instant Summaries")
                st.markdown("- 👥 Non-tech Friendly")

        st.markdown("---")

        # Smart Weather Monitoring
        with st.expander("🌦️ Smart Weather Monitoring Station for Agriculture"):
            c1, c2 = st.columns([2, 1])
            with c1:
                st.markdown("**Stack:** Arduino UNO · Python · Matplotlib · Streamlit · IoT")
                st.write("""
                Low-cost smart weather monitoring station for agriculture. Arduino UNO reads 
                temperature, humidity, rainfall, and soil moisture sensors in real time. Data 
                is streamed to an interactive Python dashboard for live charts and historical 
                trend analysis, helping farmers make better irrigation decisions.

                **Key Features:**
                - Multi-sensor data acquisition (temp, humidity, rainfall, soil moisture)
                - Real-time interactive dashboard with live charts
                - Historical trend analysis and threshold alerts
                - Designed for low-cost rural deployment
                """)
                if st.button("View on GitHub", key="g_weather"):
                    st.write("🔗 [GitHub](https://github.com/Sidd2465)")
            with c2:
                st.markdown("**Status:** ✅ Completed")
                st.markdown("- 🌱 Agricultural Focus")
                st.markdown("- 📊 Interactive Dashboard")
                st.markdown("- 🔌 Arduino UNO + Python")

        st.markdown("---")

        # Face Recognition
        with st.expander("👁️ Real-Time Face Recognition System"):
            c1, c2 = st.columns([2, 1])
            with c1:
                st.markdown("**Stack:** Python · OpenCV · TensorFlow · Deep Learning")
                st.write("""
                Real-time face recognition system using OpenCV and deep learning facial embeddings. 
                The pipeline covers detection, alignment, embedding extraction, and identity 
                classification from a live webcam feed.

                **Key Features:**
                - Real-time face detection & recognition
                - Deep learning embedding pipeline
                - Scalable to multi-person recognition
                - High accuracy across varied lighting
                """)
                if st.button("View on GitHub", key="g_face"):
                    st.write("🔗 [GitHub](https://github.com/Sidd2465)")
            with c2:
                st.markdown("**Status:** ✅ Completed")
                st.markdown("- 🎯 Real-time Pipeline")
                st.markdown("- 🧠 Deep Learning")
                st.markdown("- 📸 Live Camera Feed")

        st.markdown('</div>', unsafe_allow_html=True)

    # ── HARDWARE ──────────────────────────────
    with tab_hw:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### Hardware & Embedded Systems Projects")

        # EcoSentinel
        with st.expander("🚤 EcoSentinel — Smart Water Quality Monitoring & Sampling Boat  🏆 Innovation Award", expanded=True):
            c1, c2 = st.columns([2, 1])
            with c1:
                st.markdown("**Stack:** Embedded C · Microcontroller · pH/Turbidity/DO Sensors · Wireless · Autonomous Navigation")
                st.write("""
                Autonomous water-surface vehicle for real-time environmental water quality monitoring 
                and sampling. EcoSentinel navigates water bodies independently, collecting and 
                transmitting sensor data to a remote dashboard.

                **Key Features:**
                - pH, turbidity, temperature & dissolved oxygen sensor integration
                - Wireless real-time data transmission to remote dashboard
                - Autonomous surface navigation
                - Modular firmware for easy sensor addition
                - 🏆 **Won Innovation Award — AI for Sustainability Hackathon 2026**
                """)
                if st.button("View on GitHub", key="g_eco"):
                    st.write("🔗 [GitHub](https://github.com/Sidd2465)")
            with c2:
                st.markdown("""
                    <div style="background:linear-gradient(135deg,rgba(255,217,61,0.2),rgba(255,169,61,0.1));
                                border:1px solid rgba(255,217,61,0.5);border-radius:15px;padding:15px;text-align:center;">
                        <p style="color:#FFD93D;font-weight:700;font-size:1.1em;margin:0 0 5px 0;">🏆 Innovation Award</p>
                        <p style="color:#cccccc;font-size:0.85em;margin:0;">AI for Sustainability<br>Hackathon 2026<br>Canadian Univ. Dubai</p>
                    </div>
                """, unsafe_allow_html=True)

        st.markdown("---")

        # Smart Track Recording Car
        with st.expander("🚗 Smart Track Recording Car — Smart India Hackathon 2025"):
            c1, c2 = st.columns([2, 1])
            with c1:
                st.markdown("**Stack:** Embedded C · Arduino/STM32 · Encoders · IMU · GPS · Data Logging")
                st.write("""
                An embedded-system-powered car built for SIH 2025 that autonomously records and maps 
                vehicle tracks in real time using sensor fusion.

                **Key Features:**
                - Encoder + IMU + GPS sensor fusion for accurate path tracking
                - Onboard data logging to flash/SD storage
                - Wireless transmission of recorded track data
                - Modular firmware for sensor swapping
                """)
            with c2:
                st.markdown("**Status:** ✅ Completed")
                st.markdown("**Achievement:** 🏅 SIH 2025 Participant")

        st.markdown("---")

        # Hand Gesture Glove
        with st.expander("🖐️ Hand Gesture Detection Glove & Web Application"):
            c1, c2 = st.columns([2, 1])
            with c1:
                st.markdown("**Stack:** ESP32 · Flex Sensors · Python · OpenCV · Scikit-learn · Streamlit/Flask")
                st.write("""
                Wearable glove with flex sensors on an ESP32 that classifies hand gestures in real time. 
                A companion web app supports recognition via both the hardware glove and a live camera 
                feed using computer vision.

                **Key Features:**
                - Flex sensor array wired to ESP32 for real-time gesture capture
                - ML model for gesture classification (5+ gesture types)
                - Dual input mode: wearable glove OR camera (OpenCV)
                - Streamlit/Flask interface with live gesture display
                """)
                if st.button("View on GitHub", key="g_glove"):
                    st.write("🔗 [GitHub](https://github.com/Sidd2465)")
            with c2:
                st.markdown("**Status:** ✅ Completed")
                st.markdown("- 🖥️ Dual Input Mode")
                st.markdown("- 🤖 ML Classification")
                st.markdown("- 📡 ESP32 Wireless")

        st.markdown("---")

        # Smart Atmospheric Water Generator
        with st.expander("💧 Smart Atmospheric Water Generator"):
            c1, c2 = st.columns([2, 1])
            with c1:
                st.markdown("**Stack:** Embedded C · Arduino · Temp/Humidity/Pressure Sensors · Control Algorithms")
                st.write("""
                Embedded system that generates potable water from atmospheric humidity. 
                Automated control algorithms optimise cooling cycles for maximum yield 
                at minimum energy consumption.
                """)
            with c2:
                st.markdown("**Status:** ✅ Completed")
                st.markdown("**Focus:** 🌱 Sustainability")

        st.markdown("---")

        # Robotic Arm
        with st.expander("🦾 Robotic Arm using DC Motors"):
            c1, c2 = st.columns([2, 1])
            with c1:
                st.markdown("**Stack:** Arduino · PWM Control · DC Motors · Modular Firmware")
                st.write("Multi-axis robotic arm with precise PWM-based DC motor control. Modular firmware for clean testing and scalability.")
                if st.button("ELC Certificate", key="cert_arm"):
                    st.info("📜 TIET ELC Activity — Robotic ARM Control (May 2025) | ID: FVtLPZtw0H")
            with c2:
                st.markdown("**Status:** ✅ Completed")
                st.markdown("**Certificate:** 📜 TIET ELC")

        st.markdown('</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════
# HACKATHONS PAGE
# ══════════════════════════════════════════════
elif st.session_state.page == 'Hackathons':
    st.markdown('<h1 class="gradient-text" style="font-size:3em;">Hackathons & Competitions</h1>', unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    # Featured award banner
    st.markdown("""
        <div style="background:linear-gradient(135deg,rgba(255,217,61,0.2),rgba(255,169,61,0.1));
                    border:2px solid rgba(255,217,61,0.5);border-radius:20px;padding:30px;text-align:center;margin-bottom:30px;">
            <h2 style="color:#FFD93D;margin:0 0 10px 0;">🏆 Innovation Award Winner</h2>
            <h3 style="color:#e0e0e0;margin:0 0 10px 0;">AI for Sustainability Hackathon 2026</h3>
            <p style="color:#cccccc;font-size:1.05em;margin:0;">
                Canadian University Dubai, UAE &amp; American Society for Engineers, USA<br>
                <strong style="color:#FFD93D;">Team Stormbreakers (T031)</strong> · 14–16 February 2026<br>
                Siddharth Singhal · Mridul Arora · Paawan Sharma · Shivij Grover<br>
                <em>Project: EcoSentinel — Smart Water Quality Monitoring &amp; Sampling Boat</em>
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Hackathon cards
    hc1, hc2, hc3 = st.columns(3)
    hackathons = [
        {"col": hc1, "icon": "🏆", "title": "AI for Sustainability Hackathon 2026", "award": "Innovation Award", "team": "Stormbreakers (T031)", "org": "Canadian University Dubai, UAE", "date": "14–16 Feb 2026", "project": "EcoSentinel — Autonomous Water Quality Monitoring Boat", "color": "#FFD93D", "cert": "SustainAI2026/Award/008"},
        {"col": hc2, "icon": "🤖", "title": "Agentic AI Hackathon 2025", "award": "Participation", "team": "EvoMinds (T036)", "org": "Ulster University, UK", "date": "11 Oct 2025", "project": "Agentic AI Application Development", "color": "#4ECDC4", "cert": "AgenticAI2025/Participant/025"},
        {"col": hc3, "icon": "🚂", "title": "Smart India Hackathon 2025", "award": "Participant", "team": "TIET Team", "org": "Government of India", "date": "2025", "project": "Smart Track Recording Car for autonomous path mapping", "color": "#FF6B6B", "cert": "SIH 2025"},
    ]
    for h in hackathons:
        with h["col"]:
            st.markdown(f"""
                <div class="glass-card" style="border-color:{h['color']}44;min-height:320px;">
                    <div style="text-align:center;margin-bottom:15px;">
                        <span style="font-size:2.5em;">{h['icon']}</span>
                        <h3 style="color:{h['color']};margin:10px 0 5px 0;font-size:0.95em;">{h['title']}</h3>
                        <span style="background:linear-gradient(135deg,{h['color']},{h['color']}99);color:#1a1a2e;padding:4px 12px;border-radius:20px;font-size:0.85em;font-weight:700;">{h['award']}</span>
                    </div>
                    <p style="color:#cccccc;margin:8px 0;font-size:0.88em;">👥 <strong>Team:</strong> {h['team']}</p>
                    <p style="color:#cccccc;margin:8px 0;font-size:0.88em;">🏛️ <strong>Organiser:</strong> {h['org']}</p>
                    <p style="color:#cccccc;margin:8px 0;font-size:0.88em;">📅 <strong>Date:</strong> {h['date']}</p>
                    <p style="color:{h['color']};margin:12px 0 0 0;font-size:0.88em;font-style:italic;">💡 {h['project']}</p>
                    <p style="color:#888;margin:8px 0 0 0;font-size:0.78em;">🆔 {h['cert']}</p>
                </div>
            """, unsafe_allow_html=True)

    # Open Source section
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown('<h2 class="gradient-text" style="text-align:center;font-size:2.5em;">Open Source Contributions</h2>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    oc1, oc2 = st.columns(2)
    with oc1:
        st.markdown("""
            <div class="glass-card" style="border-color:rgba(199,125,255,0.4);">
                <div style="text-align:center;">
                    <span style="font-size:2.5em;">🌸</span>
                    <h3 style="color:#C77DFF;margin:10px 0 5px 0;">GirlScript Summer of Code 2025</h3>
                    <span style="background:rgba(199,125,255,0.2);color:#C77DFF;padding:4px 12px;border-radius:20px;font-size:0.85em;">GSSoC 2025 · Contributor</span>
                </div>
                <p style="color:#cccccc;margin:15px 0;font-size:0.95em;">
                    Contributed to open-source projects as part of GirlScript Summer of Code — one of India's 
                    largest open-source programmes. Worked on bug fixes, feature additions, and documentation 
                    improvements across multiple repositories.
                </p>
                <p style="color:#C77DFF;font-size:0.9em;margin:0;">🔧 Bug Fixes · ✨ Feature Additions · 📚 Documentation</p>
            </div>
        """, unsafe_allow_html=True)

    with oc2:
        st.markdown("""
            <div class="glass-card" style="border-color:rgba(78,205,196,0.4);">
                <div style="text-align:center;">
                    <span style="font-size:2.5em;">🌍</span>
                    <h3 style="color:#4ECDC4;margin:10px 0 5px 0;">Open Source Connect India 2025</h3>
                    <span style="background:rgba(78,205,196,0.2);color:#4ECDC4;padding:4px 12px;border-radius:20px;font-size:0.85em;">OSCI 2025 · Contributor</span>
                </div>
                <p style="color:#cccccc;margin:15px 0;font-size:0.95em;">
                    Participated in Open Source Connect India, contributing to community-driven projects. 
                    Collaborated with developers nationwide on code contributions, code reviews, and 
                    issue resolutions.
                </p>
                <p style="color:#4ECDC4;font-size:0.9em;margin:0;">🤝 Code Contributions · 🔍 Code Reviews · 🐛 Issue Resolutions</p>
            </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════
# CONTACT PAGE
# ══════════════════════════════════════════════
elif st.session_state.page == 'Contact':
    st.markdown('<h1 class="gradient-text" style="font-size:3em;">Get In Touch</h1>', unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    col_form, col_info = st.columns([2, 1], gap="large")

    with col_form:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h3 style="color:#4ECDC4;">Send Me a Message</h3>', unsafe_allow_html=True)
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your Name *", placeholder="Enter your name")
            email = st.text_input("Your Email *", placeholder="Enter your email")
            subject = st.text_input("Subject *", placeholder="What's this about?")
            message = st.text_area("Message *", placeholder="Your message here...", height=150)
            submitted = st.form_submit_button("✉️ Send Message")
            if submitted:
                if name and email and subject and message:
                    st.success("✅ Thank you! Your message has been sent successfully!")
                    st.balloons()
                else:
                    st.error("⚠️ Please fill in all fields.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_info:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h3 style="color:#4ECDC4;">Contact Information</h3>', unsafe_allow_html=True)
        for icon, label, val in [("📧","Email","siddharthsinghal2465@gmail.com"),("📱","Phone","+91-9815315327"),("📍","Location","Chandigarh, India")]:
            st.markdown(f'<div style="background:linear-gradient(135deg,#16213e,#1a1a2e);padding:20px;border-radius:15px;margin-bottom:15px;border:1px solid rgba(255,107,107,0.2);"><p style="margin:5px 0;font-size:1.2em;">{icon} <strong>{label}</strong></p><p style="margin:5px 0;color:#FF6B6B;font-size:1.1em;">{val}</p></div>', unsafe_allow_html=True)

        st.markdown('<h3 style="color:#4ECDC4;margin-top:30px;">Connect</h3>', unsafe_allow_html=True)
        sc1, sc2, sc3 = st.columns(3)
        for col, link, color, icon, sname in [
            (sc1,"https://www.linkedin.com/in/siddharth-singhal-57243b277/","#0077B5","💼","LinkedIn"),
            (sc2,"https://github.com/Sidd2465","#333","💻","GitHub"),
            (sc3,"https://leetcode.com/singhalsiddharth250","#FFA116","🔢","LeetCode"),
        ]:
            with col:
                st.markdown(f'<a href="{link}" target="_blank" style="text-decoration:none;"><div class="social-card" style="background-color:{color};padding:20px;border-radius:15px;text-align:center;"><p style="font-size:2em;margin:0;">{icon}</p><p style="margin:10px 0;color:white;font-size:0.9em;font-weight:600;">{sname}</p></div></a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════
# RESUME PAGE
# ══════════════════════════════════════════════
elif st.session_state.page == 'Resume':
    st.markdown('<h1 class="gradient-text" style="font-size:3em;">My Resume</h1>', unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    rc1, rc2, rc3 = st.columns(3)
    with rc1:
        st.markdown('<div style="text-align:center;"><h3>📄 General Resume</h3><p>Standard format for all applications</p></div>', unsafe_allow_html=True)
        if st.button("Download Resume", key="dl_resume"):
            st.info("https://drive.google.com/file/d/1ZMbQZl2nRXo5Sd05MoCyVMH0Fskv6Thx/view?usp=drive_lin")
    with rc2:
        st.markdown('<div style="text-align:center;"><h3>🔌 Embedded Systems CV</h3><p>Specialised for hardware/embedded roles</p></div>', unsafe_allow_html=True)
        if st.button("Download Embedded Resume", key="dl_embedded"):
            st.info("https://drive.google.com/file/d/1FU0MJJn7DOXQtgZeOl0iHTYHRS-qRTSW/view?usp=drive_link")
    with rc3:
        st.markdown('<div style="text-align:center;"><h3>📋 Full CV</h3><p>Comprehensive document with all certificates</p></div>', unsafe_allow_html=True)
        if st.button("Download Full CV", key="dl_cv"):
            st.info("https://drive.google.com/file/d/1kIyaMRDpuGHOuTXBL4xZgYVf5jZLXz4p/view?usp=drive_link")

    st.markdown("<hr style='margin:30px 0;'>", unsafe_allow_html=True)
    st.markdown("### Resume Highlights")

    t1, t2, t3, t4, t5 = st.tabs(["🎓 Education", "💼 Experience", "🏆 Achievements", "🛠️ Skills", "📜 Certificates"])

    with t1:
        st.markdown("#### Thapar Institute of Engineering and Technology, Patiala")
        st.write("**B.E. in Electronics, Instrumentation and Control Engineering**")
        st.write("CGPA: 7.28 / 10 | Expected Graduation: 2027 | 📍 Patiala, India")
        st.markdown("**Relevant Coursework:** Embedded Systems · Microprocessors · Control Systems · Digital Signal Processing · Virtual Instrumentation · Data Structures · OOP · Signals and Systems · VLSI Design")

    with t2:
        st.markdown("#### Siemens Healthineers, Bangalore — Software Intern")
        st.write("📍 Bangalore, India | June 2025 – August 2025")
        st.write("""
        - Developed and enhanced a DICOM Image Resizer and Viewer for medical imaging systems
        - Implemented Bilinear, Bicubic, and Lanczos interpolation; evaluated with PSNR and SSIM
        - Applied CLAHE and windowing techniques for medical image enhancement
        - Followed complete SDLC practices and used Git for version control and branching
        """)
        st.markdown("#### Punjab Engineering College, Chandigarh — Summer Research Intern")
        st.write("📍 Chandigarh, India | June 2024 – July 2024")
        st.write("""
        - Semiconductor device fabrication and simulation (Cadence Virtuoso, HFSS Ansys)
        - FPGA programming and CNN model deployment on Xilinx FPGA PYNQ Z2
        - Hands-on semiconductor fabrication lab experience
        """)

    with t3:
        for ach in [
            "🏆 Innovation Award — AI for Sustainability Hackathon 2026 (Canadian University Dubai, UAE) | Team Stormbreakers",
            "🏅 Participant — Smart India Hackathon (SIH) 2025 | Smart Track Recording Car",
            "🤖 Participant — Agentic AI Hackathon 2025 (Ulster University, UK) | Team EvoMinds",
            "🌸 Open Source Contributor — GirlScript Summer of Code 2025 (GSSoC)",
            "🌍 Open Source Contributor — Open Source Connect India 2025 (OSCI)",
            "📜 HackerRank Software Engineer Intern Certified (Jul 2025) | ID: F76DC00958DC",
            "💼 Deloitte Technology Job Simulation — Coding & Development (Jun 2025)",
            "🛠️ TIET ELC Activity — Smart Security System (Jan 2025)",
            "🏠 TIET ELC Activity — IoT Based Home Automation (Feb 2025)",
            "🦾 TIET ELC Activity — Robotic ARM Control (May 2025)",
        ]:
            st.markdown(f"- {ach}")

    with t4:
        sk1, sk2 = st.columns(2)
        with sk1:
            st.markdown("**Programming Languages:**")
            st.write("Embedded C, C++, Python, Assembly, MATLAB, R, Verilog")
            st.markdown("**Embedded Platforms:**")
            st.write("Arduino, ESP32, STM32, Raspberry Pi")
            st.markdown("**Communication Protocols:**")
            st.write("I2C, SPI, CAN, UART, MQTT")
        with sk2:
            st.markdown("**Python Libraries:**")
            st.write("NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, TensorFlow, OpenCV, Streamlit")
            st.markdown("**EDA & Simulation:**")
            st.write("MATLAB/Simulink, Cadence Virtuoso, HFSS ANSYS, LabVIEW, Eagle, AutoCAD, SolidWorks")
            st.markdown("**Practices:**")
            st.write("Git, OOP, DSA, AI/ML, SDLC, Computer Vision, Modular Firmware Design")

    with t5:
        certs = [
            ("🏆", "Innovation Award — AI for Sustainability Hackathon 2026", "Canadian University Dubai, UAE", "SustainAI2026/Award/008", "Feb 2026"),
            ("🤖", "Certificate of Participation — Agentic AI Hackathon 2025", "Ulster University, UK", "AgenticAI2025/Participant/025", "Oct 2025"),
            ("💻", "Software Engineer Intern Certification", "HackerRank", "ID: F76DC00958DC", "Jul 2025"),
            ("💼", "Technology Job Simulation — Coding & Development", "Deloitte (via Forage)", "5i2wwT54dRzDjXzhD", "Jun 2025"),
            ("🦾", "ELC Activity — Robotic ARM Control", "Thapar Institute (TIET)", "FVtLPZtw0H", "May 2025"),
            ("🏠", "ELC Activity — IoT Based Home Automation", "Thapar Institute (TIET)", "xbfjTE5DKm", "Feb 2025"),
            ("🔒", "ELC Activity — Smart Security System", "Thapar Institute (TIET)", "Atbh1yvUwB", "Jan 2025"),
        ]
        for icon, title, issuer, cert_id, date in certs:
            st.markdown(f"""
                <div style="background:rgba(22,33,62,0.5);border:1px solid rgba(255,107,107,0.2);border-radius:15px;padding:15px;margin-bottom:10px;display:flex;justify-content:space-between;align-items:center;">
                    <div>
                        <p style="margin:0 0 4px 0;color:#e0e0e0;">{icon} <strong>{title}</strong></p>
                        <p style="margin:0;font-size:0.85em;color:#4ECDC4;">{issuer}</p>
                        <p style="margin:4px 0 0 0;font-size:0.78em;color:#888;">🆔 {cert_id}</p>
                    </div>
                    <div style="text-align:right;min-width:100px;">
                        <p style="margin:0;font-size:0.85em;color:#FF6B6B;">{date}</p>
                        <p style="margin:4px 0 0 0;font-size:0.75em;color:#888;">🔗 Add Drive Link</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)