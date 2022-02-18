console.log('main connected')

const modalBtns = [... document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const numQuestions = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const scoreToPass = modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')

    modalBody.innerHTML = `
        <div class="h5 mb-3">Сигурен ли си, че искаш да започнеш "<b>${name}</b>"?</div>
        <div class="text-muted">
            <ul>
                <li>трудност: <b>${difficulty}<b></li>
                <li>брой въпроси: <b>${numQuestions}<b></li>
                <li>необходими брой верни отговори: <b>${scoreToPass}%<b></li>
                <li>време: <b>${time}<b></li>
            </ul>
        </div>
    `
    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    })
}))
