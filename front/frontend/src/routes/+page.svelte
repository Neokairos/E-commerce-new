<script>

    import { notificationData } from "$lib/store/notificationStore";
    function onClick() {
        notificationData.set('workinggg')
    }
</script>


<button class='btn btn-light' on:click={onClick}>Click me!</button>