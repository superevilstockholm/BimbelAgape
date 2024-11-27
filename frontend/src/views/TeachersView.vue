<template>
    <!-- Hero Section -->
    <section class="px-0 mx-0 text-light">
        <div class="container-fluid mx-0 px-0">
            <div class="position-relative p-0 m-0" style="height: 700px !important;">
                <img class="position-absolute z-1" style="width: 100%; max-width: 100%; height: 100%; object-fit: cover; object-position: top; filter: brightness(50%) contrast(105%); image-rendering: crisp-edges;" src="@/assets/teachers_main_section1.jpg" alt="">
                <div class="position-absolute z-3 w-100 h-100" style="background-color: rgba(0, 0, 0, 0.15);">
                    <div class="container w-100 h-100 py-0 my-0">
                        <div class="row w-100 h-100 p-0 m-0">
                            <div class="d-flex flex-column w-100 h-100 align-items-center justify-content-center p-0 m-0">
                                <div class="d-flex flex-column w-100 p-0 m-0 align-items-center" style="animation: slideUpTextAnimation 2s ease;">
                                    <h1 class="fw-bold text-center pb-0 mb-0" style="font-size: 3.2rem; font-family: 'Inter', Helvetica, sans-serif, serif;">Teachers And Staff</h1>
                                    <p class="text-center w-75">Lorem ipsum dolor sit amet consectetur adipisicing elit. Asperiores eius modi earum, rerum nobis dicta rem, et odio sequi aliquam dolorum quae expedita, sit excepturi repellat magni obcaecati saepe nostrum.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- Teacher Section -->
    <section class="py-5 my-5">
        <div class="container">
            <h1 class="text-center mb-5">Meet Our Teachers</h1>
            <!-- Teacher Cards -->
            <div class="row g-4 mx-lg-5">
                <div class="col-lg-3 col-md-4 col-12 d-flex align-items-stretch" v-for="(teacher, index) in teachers" :key="index">
                    <div class="card shadow-lg border-light">
                        <img :src="teacher['image']" class="card-img-top" alt="Teacher 1">
                        <div class="card-body d-flex flex-column">
                            <h5 class="card-title">{{ teacher['name'] }}</h5>
                            <p class="card-text text-muted">{{ teacher['teach'] }}</p>
                            <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam.</p>
                            <a href="#" class="btn btn-primary ms-0 me-auto mt-auto mb-0">View Profile</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');

/* X-Small devices (landscape phones, 575px and below) */

/* Medium devices (tablets, 768px and up) */
@media (min-width: 768px) {

}
/* Large devices (desktops, 992px and up) */
@media (min-width: 992px) {

}
</style>
<!-- Animation -->
<style>
@keyframes slideUpTextAnimation {
    from {
        transform: translateY(200%);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}
</style>
<script>
// import gsap from 'gsap';

export default {
    data() {
        return {
            teachers: [
                {
                    'name': 'Ruth Natalia Pangaribuan',
                    'teach': 'Math',
                    'image': '/ruth_natalia.jpg'
                },
                {
                    'name': 'Aprila Safira Eka Rani',
                    'teach': 'English',
                    'image': '/assets/safira.jpg'
                },
                {
                    'name': 'Fitri Utari',
                    'teach': 'Math',
                    'image': '/assets/fitri.jpg'
                },
                {
                    'name': 'Wulan',
                    'teach': 'English',
                    'image': '/assets/wulan.jpeg'
                },
                {
                    'name': 'Leo Sin Pandi',
                    'teach': 'Calistung',
                    'image': '/assets/pandi.jpg'
                },
                {
                    'name': 'Erwin Setiawan',
                    'teach': 'Computer',
                    'image': '/assets/erwin.jpg'
                },
                {
                    'name': 'Grace Herliana',
                    'teach': 'Piano',
                    'image': '/assets/ruth_natalia.jpg'
                },
                {
                    'name': 'Ombilin Hutabarat',
                    'teach': 'Football',
                    'image': '/assets/billy.jpg'
                },
                {
                    'name': 'Hisar Martha Ganda Situmorang',
                    'teach': 'Korea',
                    'image': '/assets/ruth_natalia.jpg'
                },
                {
                    'name': 'Ramanda',
                    'teach': 'Staff Library',
                    'image': '/assets/ruth_natalia.jpg'
                }
            ]
        }
    }
}
</script>