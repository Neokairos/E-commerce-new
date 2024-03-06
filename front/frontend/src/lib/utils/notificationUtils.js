import { toast } from '@zerodevx/svelte-toast';

export function showNotification(message, duration) {
    toast.push(message, { duration: duration });
}
