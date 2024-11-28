<template>
    <footer>
        <div class="container-fluid p-0 m-0">
            <!-- Footer Content -->
            <div class="container py-3">
                <div class="row">
                    <!-- Follow Us Column -->
                    <div class="col-12 col-md-3 mb-3 mb-md-0">
                        <h5>Follow Us</h5>
                        <!-- You can add social media links here if needed -->
                        <ul class="list-unstyled" style="font-size: 0.8rem;">
                            <li v-for="(platform, index) in follow_us" v-bind:key="index"><a :href="platform['url']" class="text-decoration-none d-flex flex-row gap-2 align-items-center"><i :class="platform['icon']"></i>{{ platform['name'] }}</a></li>
                        </ul>
                    </div>
                    <!-- Contact Us Column -->
                    <div class="col-12 col-md-3 mb-3 mb-md-0">
                        <h5>Contact Us</h5>
                        <ul class="list-unstyled">
                            <li v-for="(contact, index) in contact_us" v-bind:key="index" style="font-size: 0.8rem;"><a :href="contact['url']" class="text-decoration-none">{{ contact['name'] }}</a></li>
                        </ul>
                    </div>
                    <!-- About Us Column -->
                    <div class="col-12 col-md-6">
                        <div class="d-flex flex-column h-100">
                            <h5>About Us</h5>
                            <p style="font-size: 0.8rem;">{{ about_us }}</p>
                        </div>
                    </div>
                </div>
                <!-- Copyright License -->
                <h6 class="text-center">Copyright &copy; 2024, Bjorki's Team. All rights reserved.</h6>
            </div>
        </div>
    </footer>
</template>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
* {
    font-family: 'Inter', Helvetica, sans-serif, serif;
}
a {
    color: rgb(0, 0, 0) !important;
}
</style>
<script>
export default {
    data() {
        return {
            follow_us: [
                {
                    name: "Instagram",
                    url: "instagram.com",
                    icon: "bi bi-instagram"
                },
                {
                    name: "Facebook",
                    url: "facebook.com",
                    icon: "bi bi-facebook"
                },
                {
                    name: "YouTube",
                    url: "youtube.com",
                    icon: "bi bi-youtube"
                },
                {
                    name: "Twitter",
                    url: "x.com",
                    icon: "bi bi-twitter"
                }
            ],
            contact_us: [
                {
                    name: "balilombok11@gmail.com",
                    url: "mailto:balilombok11@gmail.com"
                },
                {
                    name: "+62012345678",
                    url: "tel:+62012345678"
                }
            ],
            about_us: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Itaque ducimus quas eum eveniet mollitia.",
        }
    }
}
</script>