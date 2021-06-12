<script>
	import {onMount} from 'svelte';

	export let segment;
	$: isDark = false;
	
	onMount(() => {
		if (matchMedia && matchMedia('(prefers-color-scheme: dark)').matches) isDark = true;
		else isDark = false;
	});
</script>

<style>
	nav
	{
		position: fixed;
		z-index: 1000;
		width: 98%;
		/* border-bottom: 1px solid var(--text-color); */
		border-bottom-left-radius: 9px;
		border-bottom-right-radius: 9px;
		font-weight: 300;
		padding: 0 1em;
		background-image: linear-gradient(to right, var(--primary-color), var(--secondary-color));
	}
	@media screen and (max-width: 700px)
	{
		nav
		{
			width: 96%;
		}
	}
	.spacer
	{
		height: 4vh;
	}
	ul
	{
		margin: 0;
		padding: 0;
	}
	ul::after
	{
		content: '';
		display: block;
		clear: both;
	}
	.theme-switch
	{
		float: right;
	}
	li
	{
		font-family: 'Oswald', sans-serif;
		font-weight: 200;
		letter-spacing: 0.2vw;
		display: block;
		justify-content: conter;
		float: left;
	}
	[aria-current]
	{
		position: relative;
		display: inline-block;
	}
	[aria-current]::after
	{
		position: absolute;
		content: '';
		width: calc(100% - 1em);
		height: 2px;
		background-color: var(--secondary-color);
		display: block;
		bottom: -1px;
	}
	a, i
	{
		color: var(--text-color);
		text-decoration: none;
		padding: 1em 0.5em;
		display: block;
	}
	i
	{
		color: var(--bg-color);
	}
</style>

<svelte:head>
	{#if !isDark}
		<link rel="stylesheet" href="varlight.css">
	{:else}
		<link rel="stylesheet" href="vardark.css">
	{/if}
</svelte:head>
<nav>
	<ul>
		<li><a aria-current="{segment === undefined ? 'page' : undefined}" href=".">Adsnowa</a></li>
		<li><a aria-current="{segment === 'o_mnie' ? 'page' : undefined}" href="o_mnie">O mnie</a></li>
		<!-- <li><a aria-current="{segment === 'portfolio' ? 'page' : undefined}" href="portfolio">Portfolio</a></li> -->
		<li><a aria-current="{segment === 'kontakt' ? 'page' : undefined}" href="kontakt">Kontakt</a></li>
		<!-- <li><a aria-current="{segment === 'galeria' ? 'page' : undefined}" href="galeria">Galeria</a></li> -->
		<li><a rel=prefetch aria-current="{segment === 'wiecej' ? 'page' : undefined}" href="wiecej">Więcej</a></li>
		<li><a rel=prefetch aria-current="{segment === '2021' ? 'page' : undefined}" href="2021">2021</a></li>

		<li class="theme-switch"><i class="{isDark ? "fas fa-moon" : "fas fa-sun"}" on:click={() => isDark ? isDark = false : isDark = true}></i></li>
	</ul>
</nav>
<div class="spacer"></div>
