# 🧠 Task 05 – Descriptive Statistics with Large Language Models

## 📁 Dataset
**Title**: Cars Datasets 2025  
**Source**: [Kaggle](https://www.kaggle.com/datasets/abdulmalik1518/cars-datasets-2025)  
**Size**: ~1,200 rows × 11 columns  
**Content**: Details about cars such as company, model, engine size, horsepower, acceleration, top speed, price, fuel type, torque, and seating capacity.  
⚠️ *As instructed, the dataset file is excluded from this repository and is stored locally under `data/`.*

## 🎯 Objective
The purpose of this task was to:  
- Select a compact, public dataset.  
- Produce descriptive and analytical statistics using Python.  
- Leverage a large language model (LLM) like ChatGPT to answer natural language queries about the dataset.  
- Verify the model’s outputs against computed values.  
- Reflect on prompt design, reasoning quality, and response accuracy.  

## 🛠️ What I Did

### ✅ Step 1: Dataset Selection
I chose the Cars Datasets 2025 because it is clean, well-structured, and includes a wide range of attributes that support both numerical and reasoning-focused questions.  
🔗 [Dataset link](https://www.kaggle.com/datasets/abdulmalik1518/cars-datasets-2025?resource=download)  

### ✅ Step 2: Descriptive Statistics
I developed a Python script (`basic_stats.py`) that:  
- Parsed numeric values from formatted text.  
- Calculated key summary measures: average horsepower, acceleration, engine size, torque, and price.  
- Ranked the top 5 cars by horsepower, acceleration, and price.  
- Generated grouped summaries: horsepower and price by fuel type, horsepower by seating capacity, acceleration by fuel type.  
- Computed derived ratios including horsepower-to-price, speed-to-acceleration, and speed-to-price.  

📂 Outputs saved to:  
- `output/summary_stats.json`  
- `output/top_performers.txt`  

### ✅ Step 3: Prompting the LLM
Using ChatGPT-4o, I created a set of natural language questions about the dataset, such as:  
- *"Which car has the highest horsepower?"*  
- *"Which fuel type accelerates the fastest on average?"*  
- *"If my budget is under $100,000, which high-performance cars should I consider?"*  

I documented:  
- Each prompt used  
- The LLM’s answer  
- Whether the answer was fully correct, partially correct, or incorrect  
- Notes on refining prompts and observations of model behavior  

👉 Full details can be found in `llm_prompt_log.md`.  

## 📂 File Structure
```
Task_5/
├── .gitignore                # Ignore sensitive files and dataset
├── data/                     # Dataset (not uploaded)
│   └── Cars Datasets 2025.csv
├── output/                   # Auto-generated statistics
│   ├── summary_stats.json
│   └── top_performers.txt
├── basic_stats.py            # Python script for statistics
├── llm_prompt_log.md         # Prompt + response + validation
└── README.md                 # Project documentation
```

## 🧪 Tools Used
- Python 3.13  
- pandas, re, json, os  
- ChatGPT (GPT-4o, July 2025)  
- VS Code  

## 🧠 Key Learnings
- LLMs such as ChatGPT can process structured data effectively and give correct factual responses when prompts clearly reference column names.  
- For strategic or recommendation-style queries (e.g., best car under a price constraint), the model requires explicit metrics and clear guidance.  
- The way prompts were phrased had a major impact on accuracy—small changes often improved responses.  

## 👩‍💻 Author

**Ishita Ajay Trivedi**  
Master’s in Information Systems  
Syracuse University