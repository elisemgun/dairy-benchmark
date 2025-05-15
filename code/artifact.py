def agent(user_query) -> Command:
    """ The agent and its inner workings """
    similar_deviations = find_similar_deviations(user_query) # Result from the fuzzy search

    prompt = f"""
        You are the a domain expert specializing in milk processing factories. 
        Your responsibilities include:
        - Receive a deviation description and suggest how to solve it.
        - Reading similar past deviations and their solutions.
        - Provide 1-2 actionable suggestions to address the deviation.
        - Include past deviations that were similar, and how they were resolved in your response.

        Current deviation: {user_query}
        Similar past deviations: {similar_deviations}

        Suggest specific corrective actions to correct the deviation for the operator.
    """
    response = send_query(prompt, "deepseek-r1:32b")    # Sends the prompt and user question to deepseek
    return Command(goto=END, update={"final_answer": response}) # Ends the program and returns the final answer
