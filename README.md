# Cloud Based Encryption Service via AWS

## 📝 Overview
The **Cloud-Based Encryption Service** is a security-focused application that allows users to perform high-grade file encryption via a mobile interface. By offloading cryptographic processes to the **Amazon Web Services (AWS)** cloud, the service ensures that mobile devices can secure sensitive data without consuming heavy local processing power. The project demonstrates a full-stack integration of mobile development (React Native) and cloud infrastructure (AWS EC2, DynamoDB, and Cognito).

## ⚙️ Methodology
* **User-Centric Design:** Developed a mobile front-end for easy file interaction.
* **Security First:** Integrated **AWS Cognito** for Identity and Access Management (IAM).
* **Offloaded Computation:** Utilized a "Compute-as-a-Service" model where a dedicated **EC2 instance** handles the encryption logic.
* **Hybrid Networking:** Used a combination of SSH and SFTP protocols to manage and deploy the backend logic securely.

## 🛠️ Tools & Technologies
* **Frontend:** React Native, JavaScript, Node.js
* **Cloud Platform (AWS):** EC2 (Ubuntu), Cognito, DynamoDB, Amplify.
* **Encryption Standards:** Python-based AES, ChaCha20, Fernet.
* **Deployment Tools:** PuTTY (SSH), FileZilla (SFTP), PuTTYgen.

## 💻 Implementation

### 1. Cloud Infrastructure Setup
* Provisioned an **Ubuntu EC2 instance** on AWS using an RSA key pair (`ez-encrypt.pem`).
* **Credential Conversion:** Used **PuTTYgen** to convert the `.pem` key into a `.ppk` format.

### 2. Remote Server Configuration (via PuTTY)
Connected via SSH to prepare the environment:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip -y
mkdir encryption_service && cd encryption_service
```

### 3. Logic Deployment (via FileZilla)
- Using SFTP (Port 22), I transferred the Python encryption modules from the local development environment to the EC2 instance. This ensured the source code was encrypted during the "push" to the server.

### 4. Cryptographic Logic
The backend supports three selectable algorithms (AES, Fernet and ChaCha20). 

## 📊 Results / Findings

- **Successful Multi-Algorithm Support:** The system successfully processed files using AES, ChaCha20, and Fernet.

- **Optimized Performance:** Mobile battery and CPU usage remained low as the EC2 instance handled the mathematical overhead of encryption.

- **Secure Persistence:** User records were successfully stored in DynamoDB, and authentication was verified via Cognito.

## 🖼️ Screenshots / Diagrams / Videos

## Architecture Diagram: 

<img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/66558dda-3124-4051-b85b-bf789387acd9" />

## Demo Video:

https://github.com/user-attachments/assets/7acf10e0-fa2e-4758-b559-0fab47e5d0d5

https://github.com/user-attachments/assets/556e4abe-1483-47b5-8e05-86f9a80a7bc3

## 💡 Challenges & Lessons Learned

- **Integration Complexity:** The biggest hurdle was the networking between the React Native frontend and the Python scripts on the EC2. We learned that robust API gateways are essential for seamless     mobile-to-cloud communication.

- **Environment Management:** Managing dependencies on a remote Linux server via CLI (PuTTY) improved my proficiency in Linux administration and cloud deployment.

- **Security Protocols:** Gained hands-on experience in the difference between standard FTP and SFTP, emphasizing why Port 22 is critical for secure dev-ops.
