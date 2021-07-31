<script>
    import ScrollIndicator from "../components/ScrollIndicator.svelte";
    import SocialmediaIcons from "../components/SocialmediaIcons.svelte";
</script>

<style>
    article
    {
        margin-top: 10vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 10vmin;
    }
    h2, p
    {
        font-family: 'Oswald', sans-serif;
    }
    h2
    {
        font-weight: 400;
        letter-spacing: 0.3vw;
        font-size: 4vmin;
        width: 40vw;
    }
    p
    {
        font-weight: 200;
        letter-spacing: 0vw;
        font-size: 5vmin;
    }
    button
    {
        font-family: 'Oswald', sans-serif;
        font-weight: 200;
        letter-spacing: 0.2vw;
        border-radius: 900px;
        background-image: linear-gradient(to right, var(--primary-color), var(--secondary-color));
        border: 0px solid transparent;
        padding: 2vmin;
        color: var(--text-color);
    }
</style>

<svelte:head>
	<!-- Social media -->
	<meta property="og:title" content="adsnowa">
	<meta property="og:description" content="Adam Nowakowski - kontakt">
	<meta property="og:image" content="/logo.png">
	<meta property="og:url" content="http://adsnowa.pl">
	<meta name="twitter:title" content="Adsnowa">
	<meta name="twitter:description" content="Adam Nowakowski - kontakt">
	<meta name="twitter:image" content="/logo.png">
	<meta name="twitter:card" content="summary_large_image">
	<meta name="twitter:site" content="@adsnowa">

	<title>Adsnowa - kontakt</title>
	<meta name="description" content="adsnowa - portfolio graficzne Adama Nowakowskiego">
	<meta name="keywords" content="adsnowa, graphic, designer, grafik, Adam, Nowakowski, grafika">
</svelte:head>

<ScrollIndicator/>
<article>
    <h2>
        <p>Kontakt</p>
        adsnowa@gmail.com
    </h2>
    <a href="mailto:adsnowa@gmail.com">
        <button>Napisz!</button>
    </a>
</article>
<SocialmediaIcons/>