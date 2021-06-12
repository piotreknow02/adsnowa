<style>
    .top-scroller
    {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 5vmin;
    }
    i
    {
        font-size: 5vmin;
        color: var(--text-color);
        /* background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-image: linear-gradient(to right, var(--primary-color), var(--secondary-color)); */
    }
</style>

<div class="top-scroller">
    <i class="fas fa-arrow-circle-up" on:click="{() => window.scrollTo(0, 0)}"></i>
</div>