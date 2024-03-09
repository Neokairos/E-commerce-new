<script lang="ts">
	import { userData } from '$lib/store/userStore';
	import { navigating } from '$app/stores';
	import { loading } from '$lib/store/loadingStore';
	import { notificationData } from '$lib/store/notificationStore';
	import { fly } from 'svelte/transition';
	import { afterUpdate, onMount } from 'svelte';
	import Loader from '$lib/components/Loader/Loader.svelte';
	import Header from '$lib/components/Header/Header.svelte';
	import { showNotification } from '$lib/utils/notificationUtils';
	import { SvelteToast } from '@zerodevx/svelte-toast';
	import { getCurrentUser, browserGet } from '$lib/utils/requestUtils';
	import { variables } from '$lib/utils/constants';
	import Page from './+page.svelte';
	
	$: loading.setNavigate(!!$navigating);
	$: loading.setLoading(!!$navigating, 'Loading...');
	$: $notificationData


	onMount(async () => {
		if (browserGet('refreshToken')) {
			const [response, errs] = await getCurrentUser(
				`${variables.BASE_API_URI}/token/refresh/`,
				`${variables.BASE_API_URI}/user/`
			);
			if (errs.length <= 0) {
				userData.set(response);
			}
		}
	});

	afterUpdate(async () => {
		if ($notificationData !== '') {
			
			showNotification($notificationData,3000)
			notificationData.set('');
		}
		if (browserGet('refreshToken')) {
			const [response, _] = await getCurrentUser(
				`${variables.BASE_API_URI}/token/refresh/`,
				`${variables.BASE_API_URI}/user/`
			);
			userData.update(() => response);
		}
	});
</script>

<svelte:head><Header /></svelte:head>

<div class="top-center">
	<SvelteToast />
</div>


<main>
	<Loader />
	<slot />
</main>
