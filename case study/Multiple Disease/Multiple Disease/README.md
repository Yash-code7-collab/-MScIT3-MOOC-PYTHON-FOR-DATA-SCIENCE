# Multiple Disease Prediction using Machine Learning

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/zeel0014/Multiple_Disease_Prediction)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<img width="1848" height="613" alt="Capture" src="https://github.com/user-attachments/assets/4cde9018-1ea8-4dcd-8a52-1d6ab11f15ef" />

A Streamlit web application for predicting multiple diseases including **Diabetes**, **Heart Disease**, and **Kidney Disease** using machine learning algorithms. This project provides an intuitive interface for users to input medical information and receive instant disease predictions.

## 🚀 Live Demo

**Try the app now**: [Multiple Disease Prediction on Hugging Face](https://huggingface.co/spaces/zeel0014/Multiple_Disease_Prediction)

The application is deployed and running on Hugging Face Spaces. Click the link above to use it instantly without any installation!

## 📋 Table of Contents
- [Introduction](#-introduction)
- [Live Demo](#-live-demo)
- [Features](#-features)
- [Technologies Used](#️-technologies-used)
- [Deployment](#-deployment)
- [Setup](#-setup)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [License](#-license)

## 🎯 Introduction

The Multiple Disease Prediction project aims to create a user-friendly web application that allows users to input relevant medical information and receive predictions for different diseases. Machine learning models trained on disease-specific datasets enable accurate predictions for diabetes, heart disease, and kidney disease, making health screening more accessible.

## ✨ Features

- **User Input**: Input medical information including age, gender, blood pressure, cholesterol levels, glucose levels, and other relevant factors
- **Disease Prediction**: Utilizes trained ML models to predict the likelihood of diabetes, heart disease, and kidney disease
- **Prediction Results**: Displays predicted outcomes with clear probability indicators
- **Multiple Disease Support**: 
  - Diabetes Prediction
  - Heart Disease Prediction
  - Kidney Disease Prediction
- **User-Friendly Interface**: Intuitive sidebar navigation with clean design
- **Real-time Predictions**: Instant predictions using trained machine learning models
- **No Technical Knowledge Required**: Simple interface for anyone to use

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Streamlit Option Menu**
- **scikit-learn**
- **NumPy**
- **Pandas**
- **Pickle**

## 🌐 Deployment

This application is deployed on **Hugging Face Spaces**, a platform for hosting and sharing machine learning demos and applications.

### Hugging Face Deployment

- **Platform**: Hugging Face Spaces
- **Live URL**: https://huggingface.co/spaces/zeel0014/Multiple_Disease_Prediction
- **Status**: Running and accessible 24/7
- **Framework**: Streamlit

### Deploy Your Own

To deploy your own version on Hugging Face Spaces:

1. Create an account on [Hugging Face](https://huggingface.co/)
2. Go to [Spaces](https://huggingface.co/spaces) and click "Create new Space"
3. Select **Streamlit** as the SDK
4. Upload your project files:
   - `md.py` (main application file)
   - `requirements.txt`
   - `model/` directory with all pickle files
5. Your app will automatically build and deploy!

## 📦 Setup

Follow these steps to set up the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/zeel0014/Multiple-Disease-Prediction.git
cd Multiple-Disease-Prediction
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
## 🚀 Usage

### Option 1: Use the Online Version (Recommended)

Simply visit the deployed application on Hugging Face Spaces:
**[https://huggingface.co/spaces/zeel0014/Multiple_Disease_Prediction](https://huggingface.co/spaces/zeel0014/Multiple_Disease_Prediction)**

No installation required! Just click the link and start using the app immediately.

### Option 2: Run Locally

1. Open a terminal and navigate to the project directory
2. Navigate to the app folder:
   ```bash
   cd app
   ```
3. Start the Streamlit application:
   ```bash
   streamlit run md.py
   ```
4. Open your web browser and go to `http://localhost:8501`

## 📁 Project Structure

```
Multiple-Disease-Prediction/
│
├── app/
│   ├── md.py                          # Main Streamlit application
│   └── model/
│       ├── diabetes_random_model.pkl  # Diabetes prediction model
│       ├── diabetes_scaler.pkl        # Diabetes data scaler
│       ├── heart_linear_model.pkl     # Heart disease prediction model
│       ├── kidney_linear_model.pkl    # Kidney disease prediction model
│       └── kidney_scaler.pkl          # Kidney data scaler
│
├── dataset/
│   ├── diabetes.csv                   # Diabetes training dataset
│   ├── heart.csv                      # Heart disease training dataset
│   └── kidney_disease.csv             # Kidney disease training dataset
│
├── jupitar_file/
│   ├── Diabetes.ipynb                 # Diabetes model training notebook
│   ├── Heart.ipynb                    # Heart disease model training notebook
│   └── Kidney.ipynb                   # Kidney disease model training notebook
│
├── requirements.txt                   # Python dependencies
├── LICENSE                            # MIT License
└── README.md                          # Project documentation
```

## ⚠️ Disclaimer

This application is for educational and informational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider for medical concerns.

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

**Developed by**: [@zeel0014](https://github.com/zeel0014)  
**GitHub Repository**: [Multiple-Disease-Prediction](https://github.com/zeel0014/Multiple-Disease-Prediction)  
**Live Demo**: [Hugging Face Space](https://huggingface.co/spaces/zeel0014/Multiple_Disease_Prediction)

---

⭐ **If you find this project helpful, please consider giving it a star!**  
🚀 **Try the live demo**: [https://huggingface.co/spaces/zeel0014/Multiple_Disease_Prediction](https://huggingface.co/spaces/zeel0014/Multiple_Disease_Prediction)
