import streamlit as st
import boto3

# Page setup
st.set_page_config(page_title="Internal Knowledge Assistant")

st.title("📘 Internal Knowledge Assistant")
st.write("Ask questions based on policy documents")

# User input
question = st.text_input("Enter your question")

if question:

    client = boto3.client(
        "bedrock-agent-runtime",
        region_name="us-east-1"
    )

    response = client.retrieve_and_generate(
        input={"text": question},
        retrieveAndGenerateConfiguration={
            "knowledgeBaseConfiguration": {
                "knowledgeBaseId": "XHZTEYZPSB",
                "modelArn": "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-sonnet-20240229-v1:0"
            },
            "type": "KNOWLEDGE_BASE"
        }
    )

    answer = response["output"]["text"]
    st.success(answer)
