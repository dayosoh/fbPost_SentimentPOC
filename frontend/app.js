document.addEventListener('DOMContentLoaded', fetchPosts);

function fetchPosts() {
    fetch('http://127.0.0.1:5000/posts')
        .then(response => response.json())
        .then(posts => {
            const tableBody = document.querySelector('#postsTable tbody');
            tableBody.innerHTML = '';
            posts.forEach(post => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${post.post_text}</td>
                    <td>${post.cGPTresponse}</td>
                    <td>
                        <select onchange="updateSentiment(${post.id}, this.value)">
                            <option value="Very Positive" ${post.sentiment === 'Very Positive' ? 'selected' : ''}>Very Positive</option>
                            <option value="Positive" ${post.sentiment === 'Positive' ? 'selected' : ''}>Positive</option>
                            <option value="Neutral" ${post.sentiment === 'Neutral' ? 'selected' : ''}>Neutral</option>
                            <option value="Negative" ${post.sentiment === 'Negative' ? 'selected' : ''}>Negative</option>
                            <option value="Very Negative" ${post.sentiment === 'Very Negative' ? 'selected' : ''}>Very Negative</option>
                        </select>
                    </td>
                    <td><button onclick="saveSentiment(${post.id}, this.previousElementSibling.value)">Save</button></td>
                `;
                tableBody.appendChild(row);
            });
        });
}

function ingestPost() {
    const postText = document.getElementById('postInput').value;
    const userPrompt = document.getElementById('promptInput').value;
    
    fetch('http://127.0.0.1:5000/ingest', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ post_text: postText, user_prompt: userPrompt || null })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log('Response:', data);
        fetchPosts();
    })
    .catch(error => console.error('Error:', error));
}

function updateSentiment(postId, sentiment) {
    fetch('http://127.0.0.1:5000/update_sentiment', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ post_id: postId, sentiment: sentiment })
    })
    .then(() => {
        fetchPosts();
    });
}
