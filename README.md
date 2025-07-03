# 🧠 OCI Chat App

A simple chat interface that connects to Oracle Cloud Infrastructure (OCI) Generative AI API.

## ⚙️ Prerequisites

- Node.js (v18+ recommended)
- OCI account with access to Generative AI
- OCI CLI configured with API key (stored at `~/.oci/config`)
- Your Compartment OCID

## 🚀 Setup

1. Clone the repo:

```bash
git clone https://github.com/your-username/oci-chat-app.git
cd oci-chat-app
```

2. Install dependencies:

```bash
npm install
```

3. Update the following in `server.js`:

- `<your_compartment_ocid>` → your actual compartment OCID
- `<region>` → e.g., `us-ashburn-1`

4. Start the server:

```bash
node server.js
```

5. Open your browser:

```
http://localhost:3000
```

## 🧪 Example Prompt

```
"Write a short story about a robot that learns to paint."
```
