<template>
    <header class="p-0 m-0 fixed-top" style="background-color: rgba(0, 0, 0, 0.1); backdrop-filter: blur(2px);">
        <nav class="navbar navbar-dark navbar-expand-lg pt-lg-3">
            <div class="container">
                <RouterLink class="navbar-brand fw-medium" to="/" style="font-size: 1.07rem;">
                    <img src="@/assets/logo.svg" style="height: 30px;" alt="">
                    Bimbel Agape
                </RouterLink>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ms-auto me-0 gap-lg-4 fw-normal text-center" style="font-family: 'Inter', Helvetica, sans-serif, serif; font-size: 0.8rem;">
                        <li class="nav-item">
                            <RouterLink class="nav-link active" aria-current="page" to="/">Home</RouterLink>
                        </li>
                        <li class="nav-item dropdown">
                            <a class="nav-link active dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                Subjects
                            </a>
                            <ul class="dropdown-menu dropdown-menu-dark text-center text-lg-start" style="background-color: rgba(0, 0, 0, 0.05); top: 115% !important; font-size: 0.8rem !important;">
                                <li v-for="(subject, index) in subjects" v-bind:key="index"><RouterLink class="dropdown-item" :to="subject.url">{{ subject.name }}</RouterLink></li>
                            </ul>
                        </li>
                        <li class="nav-item">
                            <RouterLink class="nav-link active" to="/teachers">Teachers</RouterLink>
                        </li>
                        <li class="nav-item">
                            <RouterLink class="nav-link active" to="#">Gallery</RouterLink>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </header>
</template>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');

.nav-item {
    display: inline-block;
    position: relative;
}
.nav-item::after {    
    background: none repeat scroll 0 0 transparent;
    bottom: 0;
    content: "";
    display: block;
    height: 1px;
    left: 50%;
    position: absolute;
    background: #fff;
    transition: width 0.25s ease 0s, left 0.25s ease 0s;
    width: 0;
}
.nav-item:hover::after { 
    width: 100%; 
    left: 0; 
}
</style>
<script>
export default {
    data() {
        return {
            subjects: [
                {
                    'name': 'Calistung',
                    'url': '/calistung'
                },
                {
                    'name': 'Math',
                    'url': '/math'
                },
                {
                    'name': 'English',
                    'url': '/english'
                },
                {
                    'name': 'Korean',
                    'url': '/korean'
                },
                {
                    'name': 'Computer',
                    'url': '/computer'
                },
                {
                    'name': 'Piano',
                    'url': '/piano'
                },
                {
                    'name': 'Guitar',
                    'url': '/guitar'
                },
                {
                    'name': 'Vocal',
                    'url': '/vocal'
                },
                {
                    'name': 'Violin',
                    'url': '/violin'
                },
                {
                    'name': 'Taekwondo',
                    'url': '/taekwondo'
                },
                {
                    'name': 'Football',
                    'url': '/football'
                }
            ]
        }
    }
}
</script>