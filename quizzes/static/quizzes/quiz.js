console.log('quiz connected');

const url = window.location.href

const quizBox = document.getElementById('quiz-box')
let data

$.ajax({
    type: 'GET',
    url : `${url}data`,
    success: function(response){
        // console.log(response);
        data = response.data
        data.forEach(el => {
            for (const [question, answers] of Object.entries(el)){
                quizBox.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        
                    </div>
                `
            }
        });
    },
    error: function(error){
        console.log(error);
    }
})