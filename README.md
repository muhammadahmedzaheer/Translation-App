# Healthcare Translation Web App with Generative AI

This is a web-based prototype designed to enable real-time, multilingual translation between patients and healthcare providers. The application converts spoken input into text, provides a live transcript, and offers a translated version with audio playback. 

## Key Features:
- **Voice-to-Text**: Converts spoken language into a text transcript.
- **Real-time Translation**: Translates the transcript into the desired language.
- **Audio Playback**: Converts translated text into speech and allows audio playback.
- **Dual Transcript Display**: Shows both original and translated transcripts simultaneously.

---

## Issues and Setup Instructions

### Google Cloud JSON Key:
Due to security considerations, the Google Cloud JSON key used to access APIs (Speech-to-Text, Translation, and Text-to-Speech services) was removed from this repository. **For security reasons, please follow the steps below to generate your own Google Cloud JSON key and set up the project on your local machine:**

1. **Set up Google Cloud Platform (GCP):**
   - Go to [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project (or use an existing one).
   - Enable the following APIs in your project:
     - **Google Cloud Speech-to-Text API**
     - **Google Cloud Translation API**
     - **Google Cloud Text-to-Speech API**
   
2. **Generate the JSON Key:**
   - In the Google Cloud Console, navigate to the **"IAM & Admin"** section.
   - Click **"Service Accounts"**, and create a new service account with appropriate roles (e.g., "Project > Owner").
   - After creating the service account, click **"Create Key"** and choose **JSON** format.
   - Save the JSON key file to your local machine.

3. **Set Up the Environment:**
   - Place the JSON key in your project directory.
   - In the `main.py` file, ensure you specify the correct path to your JSON key file:
     ```python
     os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path_to_your_json_key.json'
     ```

---

## Running the Project

Follow these steps to run the project on your local machine:

### Prerequisites:
Ensure you have the following installed:
- **Python 3.x**
- **Pip** (Python package manager)
- **Google Cloud SDK** (for interacting with Google APIs)
- **Required Python Libraries**:
  ```bash
  pip install google-cloud-speech google-cloud-translate google-cloud-texttospeech pydub

## Running the Code:
1. Clone this repository:
```bash
git clone https://github.com/your-username/Healthcare-Translation-App.git
```
2. Navigate to the project directory:
```bash
cd Healthcare-Translation-App
```
3. Run the Python script:
```bash
python main.py
```

## Deployment:
This project was intended to be deployed on platforms like Vercel, Cursor, or V0, but due to technical limitations, deployment was not completed within the 48-hour window. However, the code and features are fully functional locally, and you can follow the instructions above to run it.

## Known Issues:
- Google Cloud JSON Key: The key used for accessing Google Cloud APIs has been removed from the repository for security reasons. Please follow the setup instructions to        generate your own key.
- Deployment Issues: Vercel faced a memory limitation of 250 MB, and Cursor was incompatible with the Python version used. These deployment platforms were not fully            operational within the project's time constraints.
- Real-time Input Complexity: The scope of the project did not include capturing microphone input in real-time, as that would have introduced additional complexity.

## Future Improvements:
- Real-Time Speech-to-Text Integration: Future versions of this app will focus on integrating live microphone input for real-time translations.
- Expanded Language Support: Additional language support can be added for broader use in global healthcare contexts.
- Improved UI/UX: Further optimization for a smoother user experience on mobile devices.
