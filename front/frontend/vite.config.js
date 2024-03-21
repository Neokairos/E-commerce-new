// vite.config.js
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import fs from 'fs';


export default defineConfig({
	plugins: [sveltekit()],

	server: {
			https: {
		  	key: fs.readFileSync('/home/neokairos/localhost-key.pem'),
		  	cert: fs.readFileSync('/home/neokairos/localhost.pem'),
		},}

	
});

   