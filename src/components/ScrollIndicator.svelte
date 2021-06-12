<script>
    import {onMount} from 'svelte';
    export let stop = 1;
    onMount(() => window.addEventListener('scroll', () => {
        const scrollVal = window.pageYOffset / (document.body.offsetHeight - window.innerHeight);
        if (scrollVal < stop) document.body.style.setProperty('--scroll', scrollVal);
    }, false));
</script>

<style>
    .scroll-indicator
    {
        /* background-color: var(--bg-color); */
        position: fixed;
        z-index: 1000;
        bottom: 30px;
        right: 30px;
        padding: 2vmin;
        border-radius: 1000px;
    }
    i
    {
        font-size: 7vmin;
        background-image: radial-gradient(var(--primary-color), var(--secondary-color));
        background-clip: text;
        -moz-background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: rotate 1s linear infinite;
        animation-play-state: paused;
        animation-delay: calc(var(--scroll) * -5s);
    }
    @keyframes rotate
    {
        from
        {
            transform: rotate(0deg);
            
        }
        to
        {
            transform: rotate(360deg);
        }
    }
</style>

<div class="scroll-indicator">
    <i class="fas fa-cog"></i>
</div>