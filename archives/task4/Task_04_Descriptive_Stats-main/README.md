# 📊 Task_04_Descriptive_Stats – Analysis Overview

This README outlines the **descriptive statistical modeling** conducted on three datasets linked to the **2024 U.S. presidential election social media activity**, applying three separate methods:

- **Pure Python**: Direct calculations with core language functions  
- **Pandas**: High-level and efficient analysis  
- **Polars**: Lightweight and fast DataFrame operations  

---

## 📁 Datasets Used

1. **Facebook Ads** → `2024_fb_ads_president_scored_anon.csv`  
2. **Facebook Posts** → `2024_fb_posts_president_scored_anon.csv`  
3. **Twitter Posts** → `2024_tw_posts_president_scored_anon.csv`  

---

## 🛠️ Steps Performed per Dataset

Each script executes the following sequence of steps:

1. **Data Inspection**  
   - Display column names and data types  
2. **Data Cleaning (if necessary)**  
   - Correct formatting (e.g., remove commas from numeric strings)  
3. **Descriptive Statistics**  
   - Calculate Count, Mean, Minimum, Maximum, and Standard Deviation  
4. **Grouped Analysis**  
   - Grouped by account/page ID  
   - Grouped by account ID and post/ad ID  

---

## 🧪 Model Implementations

| Library       | Script Example                  | Output Example                |
|---------------|----------------------------------|-------------------------------|
| Pure Python   | `pure_python_stats_ads.py`       | `pure_python_output_ads.txt`  |
| Pandas        | `pandas_stats_posts.py`          | `pandas_output_posts.txt`     |
| Polars        | `polars_stats_twitter.py`        | `polars_output_twitter.txt`   |

All methods export their summaries into `.txt` files for review and submission.  

---

## 📊 Output Summary

For numerical attributes such as:  

- `estimated_audience_size`  
- `estimated_impressions`  
- `estimated_spend`  
- Engagement metrics: `likes`, `comments`, `shares`, etc. (in posts/tweets)  

The following metrics are generated:  

- Count  
- Mean  
- Standard Deviation  
- Minimum and Maximum  
- Group-level Means (Top 10 examples)  

---

## ✅ Conclusion

This analysis establishes a reproducible foundation for investigating patterns in political ad reach and organic social engagement across different platforms. The resulting files are ready for review and reporting.  

---

## 👩‍💻 Author

**Ishita Ajay Trivedi**  
Master’s in Information Systems  
Syracuse University