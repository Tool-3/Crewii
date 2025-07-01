import streamlit as st

# Title and Description
st.title("Crewai Compliance Officers")
st.write("A platform connecting experts in Indian compliance regulations.")

# Sidebar for Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Experts", "Contact"])

# Home Page
if page == "Home":
    st.header("Welcome to Crewai")
    st.write("We are a group of experienced compliance officers from various regulatory bodies in India.")
    st.write("Our mission is to provide guidance and support on compliance issues.")

# Experts Page
elif page == "Experts":
    st.header("Our Experts")
    search_query = st.text_input("Search by name or role")

    experts = [
        {
            "name": "Dr. Jane Doe",
            "role": "Compliance Officer at SEBI (Securities and Exchange Board of India)",
            "experience": "15 years",
            "qualifications": [
                "PhD in Finance from University of Delhi",
                "Certified Public Accountant (CPA)",
                "Chartered Financial Analyst (CFA)"
            ],
            "areas_of_expertise": [
                "Financial Reporting",
                "Corporate Governance",
                "Regulatory Compliance",
                "Investment Management"
            ],
            "tasks": [
                "Conducting regular audits of financial statements and disclosures.",
                "Ensuring compliance with SEBI regulations and guidelines.",
                "Providing training and workshops for compliance teams.",
                "Handling investigations and enforcement actions."
            ]
        },
        {
            "name": "Mr. John Smith",
            "role": "Compliance Officer at RBI (Reserve Bank of India)",
            "experience": "10 years",
            "qualifications": [
                "MBA in Finance from IIM Ahmedabad",
                "Certified Anti-Money Laundering Specialist (CAMS)",
                "Chartered Accountant (CA)"
            ],
            "areas_of_expertise": [
                "Monetary Policy",
                "Capital Adequacy",
                "Anti-Money Laundering (AML)",
                "Know-Your-Customer (KYC)"
            ],
            "tasks": [
                "Monitoring and enforcing monetary policies and regulations.",
                "Conducting stress tests and capital adequacy assessments.",
                "Managing AML and KYC programs.",
                "Collaborating with international regulatory bodies."
            ]
        },
        {
            "name": "Ms. Alice Johnson",
            "role": "Compliance Officer at IRDAI (Insurance Regulatory and Development Authority of India)",
            "experience": "12 years",
            "qualifications": [
                "LLB from National Law University, Delhi",
                "Certified Insurance Manager (CIM)",
                "Chartered Insurance Professional (CIP)"
            ],
            "areas_of_expertise": [
                "Insurance Regulations",
                "Consumer Protection",
                "Fraud Prevention",
                "Product Development"
            ],
            "tasks": [
                "Regulating insurance companies and ensuring compliance with IRDAI rules.",
                "Conducting inspections and audits of insurance products and services.",
                "Developing and implementing compliance policies and procedures.",
                "Providing guidance on consumer protection and fraud prevention."
            ]
        }
    ]

    filtered_experts = [expert for expert in experts if search_query.lower() in expert["name"].lower() or search_query.lower() in expert["role"].lower()]

    for expert in filtered_experts:
        st.subheader(expert["name"])
        st.write(f"**Role:** {expert['role']}")
        st.write(f"**Experience:** {expert['experience']}")
        
        with st.expander("View Details"):
            st.subheader("Qualifications:")
            for qualification in expert["qualifications"]:
                st.write(f"- {qualification}")
            
            st.subheader("Areas of Expertise:")
            for area in expert["areas_of_expertise"]:
                st.write(f"- {area}")
            
            st.subheader("Tasks:")
            for task in expert["tasks"]:
                st.write(f"- {task}")
        st.markdown("---")


# Contact Page
elif page == "Contact":
    st.header("Contact Us")
    st.write("For any inquiries or collaborations, please contact us at:")
    st.write("Email: info@crewai.com")
    st.write("Phone: +91 1234567890")
