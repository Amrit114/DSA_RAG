function askQuestion() {
    const question = document.getElementById("question").value;
    const answerDiv = document.getElementById("answer");

    answerDiv.innerText = "Thinking...";

    fetch("/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question: question })
    })
    .then(res => res.json())
    .then(data => {
        answerDiv.innerText = data.answer;
    })
    .catch(err => {
        answerDiv.innerText = "Error occurred.";
    });
}
