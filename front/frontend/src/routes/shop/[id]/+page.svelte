<script>
	// @ts-nocheck

	import axios from 'axios';
	import { productStore } from '../../../store';
	import { onMount } from 'svelte';

	// @ts-ignore
	export let data;
	// @ts-ignore
	let product;
	let loading = true;

	onMount(async function () {
		try {
			if ($productStore.all.some((product) => product.id == data.id)) {
				product = $productStore.all.find((product) => product.id == data.id);
				loading = false;
			} else {
				const endpoint = `http://127.0.0.1:8000/api/products/${data.id}`;
				let res = await axios.get(endpoint);
				product = res.data;
				productStore.update((n) => ({ ...n, all: [...n.all, product], current: product })); 
				loading = false;
			}
		} catch (err) {
			console.log('error at Details: ', err);
			product = null;
			loading = false;
		}
	});
</script>

{#if loading}
	<div class="center">
		<div class="loader" role="status"></div>
	</div>
{:else if !loading}
	<h2 class="mb-4">{product.title}</h2>
	<div class="row mt-4">
		<div class="col-12 col-md-4">
			<img src={product.image} alt="product" class="w-100 mb-3" />
			<h5 class="mt-4">Seller: {product.seller}</h5>
			<a href="/shop/{product.id}/buy" class="btn btn-primary p-8 mt-2 pl-5">Buy</a>
			<a href="/shop" class="btn btn-danger p-8 mt-2 pr-5">Back</a>
		</div>
		<div class="col-12 col-md-8 py-2">
			<p class="mb-2">{product.description}</p>
		</div>
	</div>
{:else}
	<p>No product was found with ID {data.id}</p>
	<a href="/shop" class="btn btn-danger p-8 mt-2 pr-5">Back</a>
{/if}
