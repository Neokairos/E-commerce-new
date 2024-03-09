<script>
	// @ts-nocheck

	import axios from 'axios';
	import { onMount } from 'svelte';
	import { productStore } from '../../store';
	import { variables } from '$lib/utils/constants';
	let loading = true;
	onMount(async function () {
		try {
			if (!$productStore.all.length) {
				const endpoint = `${variables.BASE_API_URI}/products`;
				const response = await axios.get(endpoint);
				productStore.update((n) => ({ ...n, all: response.data }));
				loading = false;
			} else {
				loading = false;
			}
		} catch (err) {
			loading = false;
			console.log(err);
		}
	});
</script>

<div>
	<h2 class="my-4">Products</h2>

	{#if loading}
		<div class="center">
			<div class="loader" role="status"></div>
		</div>
	{:else}
		<div class="row">
			{#each $productStore.all as item}
				<div class="col-12 col-sm-6 col-md-4">
					<div class="card w-100 h-100">
						<img
							class="card-img-top"
							style="height: 300px; object-fit: cover; margin-left:5px"
							src={item.image}
							alt="item"
						/>

						<div class="card-body d-flex flex-column justify-content-between gap-4">
							<div>
								<h5 class="card-title">{item.title}</h5>
								<i class="card-text">Seller: <b>{item.seller}</b></i>
							</div>

							<div>
								<a href="/shop/{item.id}" class="btn btn-info">View</a>
							</div>
						</div>
					</div>
				</div>
			{/each}
		</div>
	{/if}
</div>
