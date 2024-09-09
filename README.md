# Digital Product Test Case Generator

This AI-powered tool generates test cases for digital products such as websites or mobile apps based on images (screenshots). Using **BLIP (Bootstrapping Language-Image Pretraining)** for image captioning and **Groq** for generating detailed test cases, this tool makes it easy to write test instructions for functionality, responsiveness, and UX testing.

## Features

- **Image Captioning**: Automatically generates a description of the uploaded screenshot or image.
- **Test Case Generation**: Generates test cases for functionality, responsiveness, and user experience (UX).
- **Single or Multiple Image Upload**: Upload a single image or multiple images for batch processing.
- **Support for Different Digital Products**: Generate test cases for websites, mobile apps, or any digital product.
- **Contextual Test Case Generation**: Add custom context to tailor the generated test cases.

## Technologies Used

- **Python**
- **Streamlit**: For creating the interactive user interface.
- **Hugging Face Transformers**: Using the BLIP model for image captioning.
- **Groq API**: For generating detailed test cases based on the generated captions.

## Installation

To get started, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/digital-product-test-case-generator.git
    cd digital-product-test-case-generator
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Add your **Hugging Face API Key** and **Groq API Key** to the code. 

   - **Hugging Face API Key** should replace the authorization token in the `API_URL` used for the image captioning.
   - **Groq API Key** should be added in the Groq client instantiation.
   
## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Once the app is running, you'll see options to upload images and select the type of product (website, app, or other). 

3. If you'd like, you can provide additional context to generate more specific test cases (e.g., "This app has a navigation bar on the left").

4. After uploading the images and clicking the "Generate Test Cases" button, the app will:
   - Generate an image description using the **BLIP** model.
   - Use **Groq** to generate test cases based on the description.

5. View the generated test cases and copy them for your testing process!

## Configuration

- **Multiple Images**: The tool allows you to upload and process multiple images simultaneously.
- **Custom Context**: Optionally, you can provide context (such as specific features or functionalities) to generate tailored test cases.

## Example Output

1. **Image Description**:
    - "This is a screenshot of a responsive website with a top navigation bar and a call-to-action button."

2. **Generated Test Cases**:
    - **Test Case 1**: Verify that the navigation menu items are clickable and direct the user to the correct pages.
    - **Test Case 2**: Test that the call-to-action button is functional and leads to the expected destination.
    - **Test Case 3**: Verify the website's responsiveness on different screen sizes (mobile, tablet, desktop).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
