<script>
    export let src;
    export let alt;

    function view(e)
    {
        const main = document.querySelector("#sapper");
        const bg = main.insertAdjacentElement('afterBegin', document.createElement('div'));
        bg.classList.add("bg");
        const bigImg = bg.insertAdjacentElement('afterBegin', document.createElement('img'));
        bigImg.src = e.target.src;
        bigImg.classList.add("big-img");
        const x = bigImg.insertAdjacentElement('afterEnd', document.createElement('i'));
        x.classList.add("fas");
        x.classList.add("fa-times-circle");
        x.classList.add("x");
        x.addEventListener('click', () => {
            document.querySelector(".bg").remove();
        });
    }
</script>

<style>
    .img-box
    {
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px dashed var(--accent-color);
        border-radius: 5px;
        width: 300px;
        height: 300px;
    }
    img
    {
        max-width: 30vw;
        max-height: 30vh;
    }
    img:hover
    {
        scale: 200%;
    }
</style>

<div class="img-box">
    <img src="{src}" alt="{alt}" on:click="{view}">
</div>