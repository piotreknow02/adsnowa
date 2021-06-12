<script>
    import { each } from 'svelte/internal';

    import ScrollIndicator from '../components/ScrollIndicator.svelte';
    // import TopScroller from '../components/TopScroller.svelte';
    import GalleryImg from '../components/GalleryImg.svelte';
    
    import {galleryList} from '2021';
    import logo from 'images/logo.png';
</script>

<style>
    article
    {
        margin-top: 4vh;
        margin-left: 10vw;
        margin-right: 10vw;
    }
    h1
    {
        font-family: 'Oswald', sans-serif;
        font-weight: 400;
        letter-spacing: 0.2vw;
        margin: 4vmin;
    }
    .gallery-container
    {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        row-gap: 5vh;
        column-gap: 5vw;
        justify-items: center;
    }
</style>

<svelte:head>
	<!-- Social media -->
	<meta property="og:title" content="adsnowa">
	<meta property="og:description" content="Adam Nowakowski - 2021">
	<meta property="og:image" content="{logo}">
	<meta property="og:url" content="http://adsnowa.pl">
	<meta name="twitter:title" content="Adsnowa">
	<meta name="twitter:description" content="Adam Nowakowski - 2021">
	<meta name="twitter:image" content="{logo}">
	<meta name="twitter:card" content="summary_large_image">
	<meta name="twitter:site" content="@adsnowa">

	<title>Adsnowa - 2021</title>
	<meta name="description" content="adsnowa - portfolio graficzne Adama Nowakowskiego">
	<meta name="keywords" content="adsnowa, graphic, designer, grafik, Adam, Nowakowski, grafika">
</svelte:head>

<ScrollIndicator/>
<article>
    <h1>Projekty 2021</h1>
    <div class="gallery-container">
        {#each galleryList as img}
            <GalleryImg src={"2021/" + img} alt={img.replace(".png", "").replace(".jpg", "")}/>
        {/each}
    </div>
</article>
<!-- <TopScroller/> -->