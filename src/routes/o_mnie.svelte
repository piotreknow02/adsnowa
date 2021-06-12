<script>
    import ScrollIndicator from '../components/ScrollIndicator.svelte';
    import SocialmediaIcons from '../components/SocialmediaIcons.svelte';
    //images
    import logo from 'images/logo.png';
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
        font-size: 4vmin;
        font-weight: 200;
        width: 40vw;
    }
    p
    {
        font-weight: 600;
        letter-spacing: 0.2vw;
        font-size: 5vmin;
    }
</style>

<svelte:head>
	<!-- Social media -->
	<meta property="og:title" content="adsnowa">
	<meta property="og:description" content="Adam Nowakowski - o mnie">
	<meta property="og:image" content="{logo}">
	<meta property="og:url" content="http://adsnowa.pl">
	<meta name="twitter:title" content="Adsnowa">
	<meta name="twitter:description" content="Adam Nowakowski - o mnie">
	<meta name="twitter:image" content="{logo}">
	<meta name="twitter:card" content="summary_large_image">
	<meta name="twitter:site" content="@adsnowa">

	<title>Adsnowa - o mnie</title>
	<meta name="description" content="Adsnowa - portfolio graficzne Adama Nowakowskiego">
	<meta name="keywords" content="Adsnowa, graphic, designer, grafik, Adam, Nowakowski, grafika">
</svelte:head>

<ScrollIndicator/>
    <article>
        <h2>
            <p>Trochę o mnie</p>
            Grafiką zajmuję się od 2001 roku. Zaczynałem w gazecie (choć nie od początku jako grafik) Dziennik Polski. Pracowałem tam przez 7 lat. Następnie od 2008 w Przedsiębiorstwie Produkcji Lodów KORAL. Tak do dziś wymyślam i projektuję papierki do lodów. Choć nie tylko. Oprócz opakowań; wszelkiego rodzaju outdoor, reklamy prasowe, katalogi, wizytówki, logotypy, prezentacje, korekta zdjęć, grafikę na potrzeby www, layouty pism, książek, kalendarzy, modele 3D.
        </h2>
    </article>
<SocialmediaIcons/>