# shin0biX

```diff
- 👨‍💻 Building real-time applications
+ 🔍 Exploring secure communication systems
```

<div align="center">
  <!-- Subtle animated typing effect using pure CSS -->
  <style>
    .typing-demo {
      display: inline-block;
      font-family: 'Courier New', monospace;
      font-size: 1.2em;
      color: #24292f;
    }
    .typing-text {
      display: inline-block;
      overflow: hidden;
      border-right: 2px solid #24292f;
      white-space: nowrap;
      margin: 0;
      animation: 
        typing 3.5s steps(40, end) infinite,
        blink-caret 0.75s step-end infinite;
    }
    .cursor {
      display: inline-block;
      width: 2px;
      background-color: #24292f;
    }
    @keyframes typing {
      from { width: 0 }
      to { width: 100% }
    }
    @keyframes blink-caret {
      from, to { border-color: transparent }
      50% { border-color: #24292f }
    }
  </style>
  <div class="typing-demo">
    <span class="typing-text">Developer • Builder • Learner</span>
  </div>
</div>

## About Me

I build full-stack applications with a focus on real-time communication and security-conscious design. My work centers around creating practical tools that solve real problems, particularly in the areas of video communication, authentication systems, and deployment automation.

Currently, I'm exploring cybersecurity concepts through hands-on implementation of secure authentication, encrypted communications, and defensive coding practices in my projects.

## 🛠️ Technologies & Skills

Based on actual project work:

**Backend Development**
- Python (FastAPI, Flask)
- RESTful API design
- WebSocket communication
- Authentication systems (JWT, bcrypt)
- Database modeling (SQLAlchemy, SQLite)

**Frontend Development**
- HTML5, CSS3, JavaScript (Vanilla JS)
- Tailwind CSS (via CDN)
- WebRTC (RTCPeerConnection for P2P communication)
- Responsive UI design

**DevOps & Deployment**
- Virtual environment management
- systemd service deployment
- Environment configuration (.env)
- Dependency management (requirements.txt)
- Local development setup

**Security Practices Implemented**
- Password hashing with bcrypt
- JWT-based authentication
- Secure WebSocket connections
- Input validation and sanitization
- Environment variable management for secrets

## 🚀 Featured Projects

### [Meetly](https://github.com/shin0biX/Meetly)
*Real-time WebRTC video call & chat application*

My most recent and substantial project demonstrating full-stack real-time communication capabilities:
- **Backend**: FastAPI with WebSocket signaling, JWT authentication, persistent chat storage (SQLite)
- **Frontend**: Vanilla JavaScript with WebRTC for peer-to-peer video/audio, Tailwind CSS via CDN
- **Architecture**: Peer-to-peer media flow with server-mediated signaling and chat persistence
- **Features**: User accounts, room creation/modification, persistent messaging, media controls
- **Deployment**: Includes systemd deployment script for production setup
- **Learning**: In-depth exploration of WebRTC NAT traversal, signaling protocols, and real-time data synchronization

### [StoriX](https://github.com/shin0biX/StoriX)
*Python web application with authentication and file management*

A substantial Python web application featuring:
- **Backend**: Modular Flask application with separate route handlers
- **Authentication**: User registration, login, and session management
- **File Handling**: Secure file upload/download capabilities
- **Planning System**: Task/project management features
- **Database**: SQLAlchemy ORM with SQLite backend
- **Structure**: Clean separation of concerns (models, routes, database)

### [flask-blog-app](https://github.com/shin0biX/flask-blog-app)
*CSS-focused frontend development project*

Demonstrates advanced CSS capabilities:
- **Styling**: Comprehensive CSS work (2.5+ MB of actual styling/theme development)
- **Responsive Design**: Mobile-friendly layouts and components
- **UI Components**: Custom-built interface elements
- **Animation**: CSS-based transitions and effects
- **Focus**: Pure frontend development without backend dependencies

## 📚 Currently Learning & Exploring

Based on recent project work and repository activity:

**Primary Focus**: Real-time communication systems
- WebRTC peer-to-peer connection optimization
- Signaling protocol design and implementation
- NAT traversal techniques (STUN/TURN considerations)
- Scalability considerations for mesh vs SFU architectures

**Security Exploration** (through implementation):
- Authentication system design and vulnerabilities
- Secure credential storage and management
- Encrypted communication channels
- Input validation and secure coding practices
- Environment-based secret management

**Architecture Patterns**:
- Microservice-inspired modular design (separate auth, rooms, realtime modules)
- Event-driven architectures using WebSockets
- Database modeling for relational data (users, rooms, messages)
- Deployment automation and service management

## 🔧 Project Structure Examples

From my actual work, here's how I typically organize projects:

```
ProjectName/
├── backend/
│   ├── main.py              # Application entry point
│   ├── config.py            # Configuration management
│   ├── database.py          # Database setup/ORM
│   ├── models.py            # Data models/schemas
│   └── routes/              # API route handlers
├── frontend/
│   ├── index.html           # Entry points
│   ├── components/          # Reusable UI elements
│   └── js/                  # Application logic
├── requirements.txt         # Dependencies
├── deploy.sh                # Deployment automation
└── README.md                # Documentation
```

## 📫 Connect

- GitHub: [github.com/shin0biX](https://github.com/shin0biX)
- Email: ujjwalfromkosi@gmail.com (from commit history)

---

*This profile accurately represents my actual work and learning journey. All projects, technologies, and skills described are based on verifiable repository content and commit history.*