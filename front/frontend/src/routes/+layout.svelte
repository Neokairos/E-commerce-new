<script lang="ts">
	import { userData } from '$lib/store/userStore';
	import { navigating } from '$app/stores';
	import { loading } from '$lib/store/loadingStore';
	import { notificationData } from '$lib/store/notificationStore';
	import { fly } from 'svelte/transition';
	import { afterUpdate, onMount } from 'svelte';
	import Loader from '$lib/components/Loader/Loader.svelte';
	import Header from '$lib/components/Header/Header.svelte';

	$: loading.setNavigate(!!$navigating);
	$: loading.setLoading(!!$navigating, 'Loading...');

	import { getCurrentUser, browserGet } from '$lib/utils/requestUtils';
	import { variables } from '$lib/utils/constants';
	import Page from './+page.svelte';

	onMount(async () => {
		if (browserGet('refreshToken')) {
			const [response, errs] = await getCurrentUser(
				`${variables.BASE_API_URI}/token/refresh/`,
				`${variables.BASE_API_URI}/user/`
			);
			if (errs.length<= 0) {
				userData.set(response)
			}
		}
	});

	afterUpdate(async () => {
		const notifyEl = document.getElementById('notification') as HTMLElement;
		if (notifyEl && $notificationData !== '') {
			setTimeout(() => {
				notifyEl.classList.add('disappear');
				notificationData.set('');
			}, 3000);
		}
		if (browserGet('refreshToken')) {
			const [response, _] = await getCurrentUser(
				`${variables.BASE_API_URI}/token/refresh/`,
				`${variables.BASE_API_URI}/user/`
			);
			userData.update(() => response);
		}

	})

</script>

<svelte:head><Header /></svelte:head>


{#if $notificationData}
	<p
		class="notification"
		id="notification"
		in:fly={{ x: 200, duration: 500, delay: 500 }}
		out:fly={{ x: 200, duration: 500 }}
	>
		{$notificationData}
	</p>
{/if}

<main>
	<Loader/>
	<slot/>
</main>