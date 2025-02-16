from transformers import pipeline

# 대화형 AI 모델 로드
chatbot = pipeline("text-generation", model="gpt3")

def generate_response(user_input):
    response = chatbot(user_input, max_length=50, num_return_sequences=1)
    return response[0]["generated_text"]

# 사용자와의 대화 예시
user_input = input("사용자: ")
print("챗봇:", generate_response(user_input))
