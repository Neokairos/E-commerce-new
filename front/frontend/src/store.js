// in your store file
import { writable } from 'svelte/store';

export const productStore = writable({
    all: [],
    current: null,
});
