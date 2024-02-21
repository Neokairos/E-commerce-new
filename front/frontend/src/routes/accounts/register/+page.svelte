<script lang="ts">
	import { fly } from 'svelte/transition';
	import { goto } from '$app/navigation';
	import { variables } from '$lib/utils/constants';
	import { notificationData } from '$lib/store/notificationStore';
	import { post } from '$lib/utils/requestUtils';
	import type { UserResponse } from '$lib/interfaces/user.interface';
	import type { CustomError } from '$lib/interfaces/error.interface';
	import { changeText } from '$lib/helpers/buttonText';
	import axios from 'axios';

	let email: string,
		username: string,
		password: string,
		confirmPassword: string,
		errors: Array<CustomError>;

	const submitForm = async () => {
		const [jsonRes, err] = await post(`${variables.BASE_API_URI}/register`, {
			user: {
				email: email,
				username: username,
				password: password
			}
		});
		const response: UserResponse = jsonRes;

		if (err.length > 0) {
			errors = err;
		} else if (response.user) {
			notificationData.update(() => 'Registration successfull');
			await goto('/shop');
		}
	};
	const passwordConfirm = () => (password !== confirmPassword ? false : true);
</script>

<svelte:head>
    <title>Registration Page</title>
</svelte:head>

<section class="container mt-5" in:fly={{ y:   100, duration:   500, delay:   650 }} out:fly={{ duration:   500 }}>
    <h1 class="text-center mb-4">Register</h1>
    {#if errors}
        {#each errors as error}
            <p class="text-center text-danger">{error.error}</p>
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
                {#if confirmPassword}
                    <button class="btn btn-success w-100 mt-3" type="submit" on:click={(e) => changeText(e, 'Registering...')}>
                        Register
                    </button>
                {:else}
                    <button class="btn btn-danger w-100 mt-3" type="submit"  disabled>Register</button>
                {/if}
            </div>
        </div>
    </form>
</section>