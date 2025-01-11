### Long Context RAG

The **RAG process** is designed to **obtain accurate answers within the framework of given information**.

This process is carried out as follows:

1. The **Retriever** searches for information highly relevant to the query.
2. The retrieved information is provided as **context**.
3. The **LLM** utilizes this context to generate more accurate responses.

However, since the Retriever generally relies on short and nearby text chunks, it is known to have limitations in answering high-level questions that require understanding the overall context.

To address these limitations and enable the LLM to respond accurately to questions requiring a comprehensive understanding of the text, an improved methodology known as **RAPTOR** has been developed.

---

### Results Before and After Applying RAPTOR

I compared the response results using the **HOUSEHOLD DEBT AND CREDIT REPORT (Q3 2024)** (46 pages).

## Q. Summarize the main points covered in the full article.

### Before Applying RAPTOR (Using RAG)

- The model retrieved short chunks of information based on the query.
- Responses were fragmented and lacked an understanding of the overall trends in the report.
- High-level questions about the report's broader implications were not fully addressed due to limited context.
    
    <aside>
    ✅
    
    The article is a quarterly report on household debt and credit for Q3 2024, released by the Federal Reserve Bank of New York. It is based on data from the New York Fed Consumer Credit Panel/Equifax. The report is part of the research and statistics efforts by the Center for Microeconomic Data. For further details, a data dictionary is available at the end of the report, and inquiries can be directed to Joelle Scally at the provided email address.
    
    </aside>
    

### After Applying RAPTOR

- The methodology allowed the model to process and synthesize the report's overall context.
- Responses demonstrated a comprehensive understanding of key trends and insights within the 46-page document.
- High-level questions were answered with greater accuracy, supported by broader contextual awareness.
    
    <aside>
    ✅
    
    The article covers several key points related to consumer credit data and household debt in the United States, based on data from the New York Federal Reserve and Equifax. The main points include:
    
    1. **Credit Scores and Loan Origination**: It discusses the use of Equifax Risk Score 3.0 to assess consumer credit risk and provides information on the origination of auto and mortgage loans, highlighting the market share of borrowers with high credit scores.
    2. **Collection Activities and Data Sampling**: The document notes that most collection activities are related to medical bills and utilities, with the panel designed to track household-level credit and debt, primarily using creditor-reported account information.
    3. **Delinquency and Public Records**: It provides information on delinquency rates and the flow into early delinquency, mentioning an increase in delinquency rates during the third quarter of 2024.
    4. **Age Groups and Data Discrepancies**: Age groups are redefined annually, and the document notes that unknown birth years for some individuals may affect data accuracy.
    5. **Debt Statistics and Analysis**: The report includes statistics on total debt balance, which increased to $17.94 trillion in Q3 2024, and analyzes debt by type, account numbers, and credit inquiries.
    6. **State and Age-Based Financial Data**: It presents financial data by state and age group, including debt balances, delinquency rates, and foreclosure and bankruptcy cases.
    7. **Credit Reporting Practices**: The document addresses issues with unreported accounts, foreclosure and bankruptcy rates, and sampling methods used in data analysis.
    
    Overall, the article provides a comprehensive overview of consumer credit reports and sample design, aiding financial institutions and policymakers in understanding and responding to credit market trends.
    
    </aside>
    

This comparison highlights the effectiveness of RAPTOR in overcoming the limitations of RAG, especially for complex queries requiring an understanding of the full document.
