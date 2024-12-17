<template>
    <header class="p-0 m-0 fixed-top" style="background-color: rgba(0, 0, 0, 0.3); backdrop-filter: blur(2px) brightness(80%);">
        <nav class="navbar navbar-dark navbar-expand-lg pb-lg-1 mb-lg-0 pt-lg-2">
            <div class="container">
                <RouterLink class="navbar-brand fw-semibold" to="/" style="font-size: 1.07rem;">
                    <img src="@/assets/logo.svg" style="height: 30px;" alt="">
                    Bimbel Agape
                </RouterLink>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ms-auto me-0 gap-lg-4 fw-medium text-center" style="font-family: 'Inter', Helvetica, sans-serif, serif; font-size: 0.85rem;">
                        <li class="nav-item">
                            <RouterLink class="nav-link" :class="{ active: $route.path === '/' }" aria-current="page" to="/">Home</RouterLink>
                        </li>
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                Subjects
                            </a>
                            <ul class="dropdown-menu dropdown-menu-dark text-center text-lg-start" style="background-color: rgba(0, 0, 0, 0.4); top: 115% !important; font-size: 0.8rem !important; backdrop-filter: blur(2px) brightness(80%) !important;">
                                <li v-for="(subject, index) in subjects" v-bind:key="index"><RouterLink class="dropdown-item" :to="subject.url">{{ subject.name }}</RouterLink></li>
                            </ul>
                        </li>
                        <li class="nav-item">
                            <RouterLink class="nav-link" :class="{ active: $route.path === '/teachers' }" to="/teachers">Teachers</RouterLink>
                        </li>
                        <li class="nav-item">
                            <RouterLink class="nav-link" :class="{ active: $route.path === '/gallery' }" to="#">Gallery</RouterLink>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </header>
</template>
<style scoped>
.nav-item, .dropdown-item {
    font-family: 'Inter', Helvetica, sans-serif, serif !important;
}
.nav-item {
    display: inline-block;
    position: relative;
}
.nav-item:after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 50%;
    width: 0;
    height: 1.5px;
    background-color: rgba(0, 0, 0, 0.7);
    transition: width 250ms ease, left 250ms ease;
}
.nav-item:hover:after {
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