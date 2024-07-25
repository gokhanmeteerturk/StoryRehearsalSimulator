import openai


class BaseConversationAgent:
    def __init__(self, api_key, role):
        self._api_key = api_key
        self._role = role
        self._conversations = []

    def add_conversation(self, conversation):
        self._conversations.append(conversation)

    def get_conversations(self):
        return self._conversations

    def generate_prompt(self):
        prompt = ""
        for conversation in self._conversations:
            prompt += conversation
        prompt += (("\nAbove is a conversation with an AI playing the role "
                   "of ") + self._role.name + (":\nDetails of the role are as "
                                               "follows:\n") +
                   self._role.details + "\n")
        return prompt

    def perform_task(self, task_request):
        self.add_conversation(f"User: {task_request}\n Answer as {self._role.name}: ")
        prompt = self.generate_prompt()
        answer = openai.Completion.create(
            engine="gpt-4o-mini",
            prompt=prompt,
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.7,
        )
        self.add_conversation(f"{self._role.name}: {answer.choices[0].text}")
        return answer.choices[0].text.strip()


