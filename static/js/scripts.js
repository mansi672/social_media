document.getElementById('postForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const caption = document.getElementById('caption').value;
    const image = document.getElementById('image').files[0];
    const scheduleTime = document.getElementById('scheduleTime').value;
    const platforms = Array.from(document.querySelectorAll('input[name="platforms"]:checked')).map(el => el.value);

    if (!caption || !image || !scheduleTime || platforms.length === 0) {
        alert('Please fill in all fields and select at least one platform.');
        return;
    }

    const formData = new FormData();
    formData.append('caption', caption);
    formData.append('image', image);
    formData.append('scheduleTime', scheduleTime);
    formData.append('platforms', JSON.stringify(platforms));

    fetch('/schedule-post', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Post scheduled successfully!');
        } else {
            alert('Failed to schedule post.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while scheduling the post.');
    });
});
