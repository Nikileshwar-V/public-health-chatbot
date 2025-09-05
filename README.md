# Public Health Chabot

A multilingual health assistant chatbot built using **Rasa**. This bot provides information on symptoms, prevention, and vaccines for various diseases, supporting both **English** and **Odia** languages. The bot is trained with intents for multiple diseases like Dengue, Malaria, COVID-19, Diabetes, Hypertension, Typhoid, Measles, Kala Azar, and more.

---

## 🚀 Project Directory Structure

```
public-health-chatbot/
│
├── actions/                 # Custom actions (if any)
│   └── __init__.py
│
├── data/                    # Training data
│   ├── nlu.yml              # NLU training data (intents & examples)
│   ├── rules.yml            # Rules for the bot responses
│   └── stories.yml          # Conversation stories
│
├── models/                  # Pre-trained Rasa model files (.tar.gz)
│   ├── 20250905-175706-selfish-status.tar.gz
│   └── ...                  # Other model snapshots
│
├── tests/                   # Test stories (optional)
│
├── config.yml               # Rasa pipeline and policies configuration
├── domain.yml               # Bot domain including intents, slots, and responses
├── credentials.yml          # Channels and connectors credentials
├── endpoints.yml            # Action server and model endpoints
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 📁 File Descriptions

* **actions/** – Contains Python files for custom actions. In this project, custom actions are minimal.
* **data/nlu.yml** – Defines intents and example user messages for training the bot.
* **data/rules.yml** – Defines rules for expected responses to certain intents.
* **data/stories.yml** – Example conversations to teach the bot dialogue flow.
* **models/** – Contains pre-trained Rasa models. Use these to run the chatbot directly without retraining.
* **config.yml** – Pipeline and policy configurations used for training.
* **domain.yml** – Defines intents, entities, slots, and responses that the bot can handle.
* **credentials.yml** – Configuration for connecting the bot to channels (e.g., Telegram, Slack).
* **endpoints.yml** – Defines URLs for Rasa action server and models.
* **requirements.txt** – Python libraries needed to run the bot.

---

## 💻 How to Run the Chatbot

1. **Clone the repository**

   ```bash
   git clone https://github.com/Nikileshwar-V/public-health-chatbot.git
   cd public-health-chatbot
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Place the pre-trained model**

   * If not already in `models/`, download or copy the `.tar.gz` model files into the `models/` folder.

4. **Run the bot**

   ```bash
   rasa shell
   ```

   or for serving via API:

   ```bash
   rasa run
   ```

5. **Chat with the bot**

   * Try queries like:

     * "What are the symptoms of Dengue?"
     * "How can I prevent Malaria?"
     * "Tell me about COVID-19 vaccine."

---

## 🛠️ Work Done by Team Members

| Name        | Contribution                                                                                                                                                                                                              |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nikil**   | - Created the Rasa chatbot framework.<br>- Developed intents and responses for diseases.<br>- Trained the initial models and created the pre-trained `.tar.gz` files.<br>- Added English and Odia responses.<br>- Designed NLU training data (`nlu.yml`) and conversation stories (`stories.yml`).<br>- Added rules for predictable responses (`rules.yml`).<br>- Verified bot responses, fixed errors             |
| **Gowtham** | - Collected trusted health data from WHO, ICMR, and MoHFW.<br> - Structured the data into a chatbot-friendly CSV with columns: Disease, Symptoms (EN), Prevention (EN), Vaccine Info (EN), Source Link.<br> - Translated key fields (Symptoms & Prevention) into Odia.<br> - Shared the finalized dataset with Nikil for training. |

---

## ⚙️ Notes

* **Models folder is required** to use the bot without retraining.
* **Do not include `venv` folder** in the repository; each user can create their own virtual environment.
* If the `.tar.gz` model file is too large for GitHub, share it via **Google Drive/Dropbox** and provide a link in the repo.
* To update the bot, modify the relevant files (`nlu.yml`, `stories.yml`, `domain.yml`) and retrain using:

  ```bash
  rasa train
  ```

---

## 🌐 Languages Supported

* **English**
* **Odia**

---

**Project Status:** ✅ Completed Phase 1 – Fully functional chatbot with pre-trained models.
