<script>
	import ScrollIndicator from '../components/ScrollIndicator.svelte';
	import SocialmediaIcons from '../components/SocialmediaIcons.svelte';
	// images
</script>

<style>
	.img-box
	{
		width: 100%;
		overflow: hidden;
	}
	img
	{
		width: 100%;
		filter: brightness(1) blur(calc(var(--scroll) * 20px));
		-webkit-filter: brightness(1) blur(calc(var(--scroll) * 20px));
	}
	@media screen and (max-width: 1030px)
	{
		img
		{
			height: 100vh;
			width: auto;
		}
	}
	.darken
	{
		filter: brightness(0);
	}
	h1
	{
		font-family: 'Oswald', sans-serif;
		font-size: 5vmin;
		position: absolute;
		font-weight: 400;
		top: 20%;
		right: 30%;
		letter-spacing: 0.5vw;
		transform: translate(50%, 0%);
		text-transform: lowercase;
		/* text-shadow: 5px 5px 15px var(--bg-color) ; */
	}
	h2
	{
		font-family: 'Oswald', sans-serif;
		font-size: 2vmin;
		font-weight: 400;
		letter-spacing: 1.2vw;
		text-transform: lowercase;
		position: absolute;
		top: 25%;
		right: 30%;
		transform: translate(50%, 0%);
		/* text-shadow: 5px 5px 15px var(--bg-color) ; */
	}
	.adam
	{
		font-weight: 200;
	}
	.nowakowski
	{
		font-weight: 600;
	}
	.graphic
	{
		font-weight: 600;
	}
	.designer
	{
		font-weight: 200;
	}
</style>

<svelte:head>
	<!-- Social media -->
	<meta property="og:title" content="adsnowa">
	<meta property="og:description" content="Adam Nowakowski - portfolio graficzne">
	<meta property="og:image" content="/logo.png">
	<meta property="og:url" content="http://adsnowa.pl">
	<meta name="twitter:title" content="Adsnowa">
	<meta name="twitter:description" content="Adam Nowakowski - portfolio graficzne">
	<meta name="twitter:image" content="/logo.png">
	<meta name="twitter:card" content="summary_large_image">
	<meta name="twitter:site" content="@adsnowa">

	<!-- google verification -->
	<meta name="google-site-verification" content="XcxqVGM3UMKyXogxLECDdFREuMfTsQS0rScVU9MZSOI" />

	<title>Adsnowa - graphic designer</title>
	<meta name="description" content="adsnowa - portfolio graficzne Adama Nowakowskiego">
	<meta name="keywords" content="adsnowa, graphic, designer, grafik, Adam, Nowakowski, grafika">
</svelte:head>

<ScrollIndicator stop={0.98}/>
<div class="img-box">
	<img src="/Me.jpeg" alt="Adam Nowakowski" class="darken" on:load="{(e) => e.target.classList.remove("darken")}">
</div>
<div class="text-container">
	<h1>
		<span class="adam">Adam</span><span class="nowakowski">Nowakowski</span>
	</h1>
	<h2>
		<span class="graphic">Graphic</span><span class="designer">Designer</span>
	</h2>
</div>