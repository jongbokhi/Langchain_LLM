# Long Context RAG

## Overview

The **RAG process** is designed to **obtain accurate answers within the framework of given information**. This process involves:

1. **Retriever**: Searches for information highly relevant to the query.
2. **Context**: Provides the retrieved information as context.
3. **LLM**: Utilizes this context to generate accurate responses.

### Limitations of RAG
- The Retriever generally relies on short, nearby text chunks.
- Struggles to answer high-level questions requiring a comprehensive understanding of the overall context.

### RAPTOR Methodology
To address these limitations and enable the LLM to respond accurately to questions requiring a comprehensive understanding of the text, an improved methodology known as **RAPTOR** has been developed.

---

## Results:

The comparison was conducted using the **HOUSEHOLD DEBT AND CREDIT REPORT (Q3 2024)** (46 pages). 

Below are the responses to the query:  
**Q: "Summarize the main points covered in the full article."**

### Before Applying RAPTOR

**✅Answer**:  
The report is a quarterly report on household debt and credit for Q3 2024, released by the Federal Reserve Bank of New York. It is based on data from the New York Fed Consumer Credit Panel/Equifax. The report is part of the research and statistics efforts by the Center for Microeconomic Data. For further details, a data dictionary is available at the end of the report, and inquiries can be directed to Joelle Scally at the provided email address.

- The model retrieved short chunks of information relevant to the query.
- Responses were fragmented, focusing on isolated details.
- High-level questions about broader trends and implications were not fully addressed.

---

### After Applying RAPTOR

**✅Answer**:  
The report covers several key points related to consumer credit data and household debt in the United States, based on data from the New York Federal Reserve and Equifax. 

The main points include:

1. **Credit Scores and Loan Origination**: Discusses the use of Equifax Risk Score 3.0 and market trends in auto and mortgage loan origination.
2. **Collection Activities**: Notes that most collection activities are related to medical bills and utilities.
3. **Delinquency Rates**: Reports an increase in delinquency rates during Q3 2024.
4. **Age Groups and Data Accuracy**: Highlights annual redefinition of age groups and potential data discrepancies due to unknown birth years.
5. **Debt Statistics**: Analyzes debt types, total debt balance ($17.94 trillion), and credit inquiries in Q3 2024.
6. **State and Age-Based Data**: Provides insights on debt balances, delinquency rates, and financial data by state and age group.
7. **Credit Reporting Practices**: Addresses issues with unreported accounts, foreclosure rates, and data sampling methods.
   
---

**💡Key Improvements**:  
- RAPTOR enabled the model to synthesize the document's overall context.  
- Responses demonstrated a comprehensive understanding of trends and insights.  
- High-level questions were answered with greater accuracy and contextual awareness.

---

## Conclusion

This comparison highlights the effectiveness of RAPTOR in overcoming the limitations of RAG, particularly for complex queries requiring an understanding of the full document. By leveraging RAPTOR, it is possible to achieve more accurate and contextually rich responses in long-text scenarios.

