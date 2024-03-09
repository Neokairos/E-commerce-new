<script lang="ts">
	import { fly } from 'svelte/transition';
	import { goto } from '$app/navigation';
	import { variables } from '$lib/utils/constants';
	import { notificationData } from '$lib/store/notificationStore';
	import { post } from '$lib/utils/requestUtils';
	import type { UserResponse } from '$lib/interfaces/user.interface';
	import { type CustomError } from '$lib/interfaces/error.interface';
	import { changeText } from '$lib/helpers/buttonText';
	import { quartOut } from 'svelte/easing';
    import { showNotification } from '$lib/utils/notificationUtils'
	import { userData } from '$lib/store/userStore';
  

	let email: string,
		username: string,
		password: string,
		confirmPassword: string,
		errors: Array<CustomError>;

	const submitForm = async () => {
		const [jsonRes, err, status] = await post(`${variables.BASE_API_URI}/register`, {
			user: {
				email: email,
				username: username, 
				password: password
			}
		});
		const response: UserResponse = jsonRes;
        const status_code: number = status

		if (err.length > 0) {
			errors = err;
		} 
		if (status_code === 201) {
			notificationData.set('Registration Succesfully done!!')
			
			setTimeout(() =>{
                goto('/shop');
            }, 2000)
			if (response.user) {
        		userData.set(response.user);
    		} else {
				console.error('no user object in the response: Response:', response.user)
			}
		} else {
			notificationData.set('Registration Failed please try again..')
            setTimeout(()=> {
                goto('/accounts/register');
            }, 1500)
        }
	};
	$: passwordConfirm = () => password === confirmPassword;
</script>

<svelte:head>
	<title>Registration Page</title>
</svelte:head>

<section
	class="container mt-5"
	in:fly={{ y: 100, duration: 500, delay: 650 }}
	out:fly={{ duration: 500 }}
>


	<h1 class="text-center mb-4">Register</h1>
	{#if errors}
		{#each errors as error (error.error)}
			<p
				class="text-center text-danger"
				transition:fly={{ y: 20, duration: 500, easing: quartOut }}
			>
				{error.error}
			</p>
		{/each}
	{/if}
	<form class="form" on:submit|preventDefault={submitForm}>
		<!-- Each input field is wrapped in a Bootstrap row and centered -->
		<div class="row justify-content-center">
			<div class="col-12 col-md-6">
				<input
					bind:value={username}
					type="text"
					class="form-control mb-3"
					aria-label="Username"
					placeholder="Username"
					required
				/>
			</div>
		</div>
		<div class="row justify-content-center">
			<div class="col-12 col-md-6">
				<input
					bind:value={email}
					type="email"
					class="form-control mb-3"
					aria-label="Email address"
					placeholder="Email address"
					required
				/>
			</div>
		</div>
		<div class="row justify-content-center">
			<div class="col-12 col-md-6">
				<input
					bind:value={password}
					type="password"
					class="form-control mb-3"
					name="password"
					aria-label="Password"
					placeholder="Password"
					required
				/>
			</div>
		</div>
		<div class="row justify-content-center">
			<div class="col-12 col-md-6">
				<input
					bind:value={confirmPassword}
					type="password"
					class="form-control mb-3"
					name="confirmPassword"
					aria-label="Confirm password"
					placeholder="Confirm your password"
					required
				/>
			</div>
		</div>
		<!-- Button is wrapped in a Bootstrap row and centered -->
		<div class="row justify-content-center">
			<div class="col-12 col-md-6">
				{#if passwordConfirm()}
					<button
						class="btn btn-success w-100 mt-3"
						type="submit"
						on:click={(e) => changeText(e, 'Registering...')}
						aria-label="Register"
						title="Click to Register"
					>
						Register
					</button>
				{:else}
					<div class="text-danger">Passwords do not match</div>
					<button
						class="btn btn-danger w-100 mt-3"
						type="submit"
						disabled
						aria-disabled="true"
						aria-label="Register"
						title="Passwords do not match">Register</button
					>
				{/if}
			</div>
		</div>
	</form>
</section>
