<template>
    <!-- Hero Section -->
    <section class="px-0 mx-0 text-light">
        <div class="container-fluid mx-0 px-0">
            <div class="position-relative p-0 m-0" style="height: 700px !important;">
                <img class="position-absolute z-1" style="width: 100%; max-width: 100%; height: 100%; object-fit: cover; object-position: top; filter: brightness(65%) contrast(100%); image-rendering: crisp-edges; pointer-events: none;" src="/assets/teachers_main_section1.webp" alt="">
                <div class="position-absolute z-3 w-100 h-100" style="background-color: rgba(0, 0, 0, 0.17);">
                    <div class="container w-100 h-100 py-0 my-0">
                        <div class="row w-100 h-100 p-0 m-0">
                            <div class="d-flex flex-c   olumn w-100 h-100 align-items-center justify-content-center p-0 m-0">
                                <div class="d-flex flex-column w-100 p-0 m-0 align-items-center" style="animation: slideUpTextAnimation 2s ease;">
                                    <h1 class="fw-bold text-center pb-0 mb-0 hero-section-title-responsive" style="font-family: 'Inter', Helvetica, sans-serif, serif;">Teachers And Staff</h1>
                                    <p class="text-center hero-section-description-responsive">“Our dedicated teachers and staff are the backbone of our educational community. With a passion for teaching and a commitment to excellence, they work tirelessly to inspire and guide students toward achieving their full potential. Get to know the talented professionals who shape our learning environment.”</p>
                                    <a href="#teachers" class="btn btn-dark fw-medium mt-2 border d-flex flex-row align-items-center gap-2" style="background-color: transparent !important; font-family: 'Inter', Helvetica, sans-serif, serif;">See Our Teachers <i class="bi bi-arrow-right"></i></a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- Teacher Section -->
    <section class="pt-5 mt-5 px-0 mx-0">
        <div class="container">
            <h1 class="text-center mb-5 fw-medium" style="font-family: 'Open Sans', 'Inter', Helvetica, sans-serif, serif !important; font-size: 3.5rem;">Meet Our Teachers</h1>
            <div class="d-flex justify-content-center mb-4">
                <select v-model="selectedSubject" class="form-select w-50">
                    <option value="">All Subjects</option>
                    <option v-for="subject in subjects" :value="subject" :key="subject">{{ subject }}</option>
                </select>
            </div>
            <!-- Modal -->
            <div class="modal" id="teacherDetailsModal" tabindex="-1" aria-hidden="true">
                <div class="modal-dialog modal-md modal-dialog-centered modal-dialog-scrollable">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">Teacher Details</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <!-- Gambar Teacher di bagian atas -->
                            <div class="mb-4">
                                <img :src="teacherModalData.image" alt="Teacher Image" class="img-fluid w-100">
                            </div>
                            <!-- Daftar Data Teacher di bawah gambar -->
                            <ul style="list-style: none;">
                                <li v-for="(value, key, index) in teacherModalData" :key="index">
                                    <div class="row d-flex flex-row align-items-center mb-2">
                                        <div class="col-4 fw-bold">{{ key }}</div>
                                        <div class="col-1">:</div>
                                        <div class="col-7">{{ value }}</div>
                                    </div>
                                </li>
                            </ul>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button type="button" class="btn btn-primary">Save changes</button>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Teacher Cards -->
            <div class="row g-4 mx-md-0 mx-3" id="teachers">
                <div class="col-lg-3 col-md-4 col-12 d-flex align-items-stretch" v-for="(teacher, index) in filteredTeachers" :key="index">
                    <div class="card shadow-lg border-light border-0">
                        <img :src="teacher.image" class="card-img-top border-0 p-0 m-0" loading="lazy" tyle="filter: brightness(80%)" alt="Teacher 1">
                        <div class="card-body d-flex flex-column border-0">
                            <h5 class="card-title mb-0">{{ teacher.name }}</h5>
                            <i>
                                <p class="card-text text-muted mb-1">
                                    <span v-for="(subject, idx) in teacher.teach" :key="idx">
                                        {{ subject }}<span v-if="idx < teacher.teach.length - 1">, </span>
                                    </span>
                                </p>
                            </i>
                            <p class="card-text">{{ teacher.description }}</p>
                            <button @click="showTeacherModalDetails(teacher)" data-bs-toggle="modal" data-bs-target="#teacherDetailsModal" type="button" class="btn btn-primary ms-0 me-auto mt-auto mb-0 px-2 py-1" style="font-size: 0.85rem;">View Profile</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- Teachers Summary -->
    <section class="py-5 my-5 py-lg-0 my-lg-0 pt-lg-5 mt-lg-5 px-0 mx-0">
        <div class="container">
            <h1 class="text-center fw-medium" style="font-family: 'opsz', 'Inter', Helvetica, sans-serif, serif; font-size: 3.5rem;">Teachers Summary</h1>
        </div>
        <div class="container-fluid p-0 m-0 responsive-other-section">
            <div class="container w-100 h-100 py-0 my-0">
                <div class="position-relative d-flex flex-column w-100 h-100 p-0 m-0 align-items-center justify-content-center">
                    <img class="bg-image-other-details-section position-absolute z-1 p-0 m-0" loading="lazy" src="/assets/teacher_icon.svg" alt="">
                    <!-- item 1 -->
                    <div class="other-section-item-1 position-absolute z-3 d-inline-flex flex-row align-items-center px-4 py-2 gap-2 border border-2 rounded-3" style="background-color: transparent; font-family: 'Inter', Helvetica, sans-serif, serif; border-color: rgba(33, 37, 41, 0.7) !important" data-bs-toggle="tooltip" data-bs-placement="top" title="Jumlah guru dan staff adalah 23">
                        <!-- Item Icon -->
                        <img class="other-section-image-responsive" loading="lazy" src="/assets/teach.png" alt="">
                        <div class="d-flex flex-column gap-0">
                            <!-- Counting -->
                            <h5 class="p-0 m-0 fw-bold">23</h5>
                            <!-- Details -->
                            <h6 class="p-0 m-0 fw-normal">Teachers & Staff</h6>
                        </div>
                    </div>
                    <!-- item 2 -->
                    <div class="other-section-item-2 position-absolute z-3 d-inline-flex flex-row align-items-center px-4 py-2 gap-2 border border-2 rounded-3" style="background-color: transparent; font-family: 'Inter', Helvetica, sans-serif, serif; border-color: rgba(33, 37, 41, 0.7) !important" data-bs-toggle="tooltip" data-bs-placement="top" title="Jumlah guru dan staff perempuan adalah 14">
                        <!-- Item Icon -->
                        <img class="other-section-image-responsive" loading="lazy" src="/assets/female-teacher.png" alt="">
                        <div class="d-flex flex-column gap-0">
                            <!-- Counting -->
                            <h5 class="p-0 m-0 fw-bold">14</h5>
                            <!-- Details -->
                            <h6 class="p-0 m-0 fw-normal">Female Teachers & Staff</h6>
                        </div>
                    </div>
                    <!-- item 3 -->
                    <div class="other-section-item-3 position-absolute z-3 d-inline-flex flex-row align-items-center px-4 py-2 gap-2 border border-2 rounded-3" style="background-color: transparent; font-family: 'Inter', Helvetica, sans-serif, serif; border-color: rgba(33, 37, 41, 0.7) !important" data-bs-toggle="tooltip" data-bs-placement="top" title="Jumlah guru dan staff laki laki adalah 9">
                        <!-- Item Icon -->
                        <img class="other-section-image-responsive" loading="lazy" src="/assets/male-teacher.png" alt="">
                        <div class="d-flex flex-column gap-0">
                            <!-- Counting -->
                            <h5 class="p-0 m-0 fw-bold">9</h5>
                            <!-- Details -->
                            <h6 class="p-0 m-0 fw-normal">Male Teachers & Staff</h6>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
<!-- Start Responsive Styling CSS -->
<style>
/* X-Small devices (landscape phones, 575px and below) */
.hero-section-title-responsive {
    font-size: 2.7rem;
}
.hero-section-description-responsive {
    width: 90%;
    font-size: 0.85rem;
}
.card-title {
    font-size: 1.05rem;
}
.card-text {
    font-size: 0.8rem;
}
.card-img-top {
    filter: brightness(80%);
    backface-visibility: hidden;
    transition: filter 300ms ease;
}
.card {
    animation: opacityCardAnimation 0.6s ease-out forwards;
    animation-timeline: view(block 130% 0%);
    transition: transform 350ms ease, box-shadow 350ms ease;
}
.card:hover {
    transform: scale(1.05);
    backface-visibility: hidden;
    box-shadow: 0 0 10px 3px rgba(0, 0, 0, 0.2) !important;
}
.card:hover .card-img-top {
    filter: brightness(105%) !important;
}
.responsive-other-section {
    height: 500px;
}
.bg-image-other-details-section {
    height: 50%;
}
.other-section-item-1 h5, .other-section-item-2 h5, .other-section-item-3 h5 {
    font-size: 1rem;
}
.other-section-item-1 h6, .other-section-item-2 h6, .other-section-item-3 h6 {
    font-size: 0.8rem;
}
.other-section-image-responsive {
    height: 30px
}
.other-section-item-1 {
    left: auto;
    right: auto;
    top: 10%;
}
.other-section-item-2 {
    right: 6%;
    top: 97%;
}
.other-section-item-3 {
    left: 6%;
    top: 80%;
}
/* Medium devices (tablets, 768px and up) */
@media (min-width: 768px) {

}
/* Large devices (desktops, 992px and up) */
@media (min-width: 992px) {
    .card-text {
        font-size: 1rem !important;
    }
    .hero-section-title-responsive {
        font-size: 3.5rem;
    }
    .hero-section-description-responsive {
        width: 75% !important;
        font-size: 1rem !important;
    }
    .responsive-other-section {
        height: 700px !important;
    }
    .bg-image-other-details-section {
        height: 50% !important;
    }
    .other-section-image-responsive {
        height: 45px !important;
    }
    .other-section-item-1 {
        right: 20% !important;
        top: 12% !important;
    }
    .other-section-item-2 {
        left: 10% !important;
        right: auto !important;
        top: 30% !important;
    }
    .other-section-item-3 {
        left: auto !important;
        right: 10% !important;
        top: 60% !important;
    }
}
</style>
<!-- End Responsive Styling CSS -->
<!-- Start Animation -->
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
@keyframes opacityCardAnimation {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}
</style>
<!-- End Animation -->
<script>
import axios from 'axios';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.min.js'

// Initialize tooltips
document.addEventListener('DOMContentLoaded', function () {
  var tooltipTriggerList = Array.from(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });
});

export default {
    data() {
        return {
            heroSectionBackgroundImages: ['teachers_main_section.jpeg', 'teachers_main_section1.jpg'], // Image name for hero section
            teachers: [], // Teachers data
            selectedSubject: "", // Selected subject for filtering specific major teachers
            teacherModalData: { // Teachers modal data
                'name': null,
                'teach': null,
                'image': null,
                'description': null,
                'gender': null,
                'age': null,
                'experience': null,
                'quote': null
            }
        }
    },
    async mounted() {
        await this.l(),
        await this.getTeachersViewPageData()
    },
    methods: {
        async l() {
            await axios.get(
                '/l',
                {
                    headers: {
                        "ngrok-skip-browser-warning": "69420"
                    }
                }
            )
        },
        // Get all teachers data
        async getTeachersViewPageData() {
            await axios.get(
                '/getTeachersViewPageData',
                {
                    headers: {
                        "ngrok-skip-browser-warning": "69420"
                    }
                }
            ).then((response) => {
                this.teachers = response.data.teachers
            }).catch((error) => {
                console.error("Error:", error)
                alert("Gagal mendapatkan data guru, harap refresh halaman!")
                this.teachers = []
            })
        },
        async getspecificTeacherModalData(id) {
            console.log(id)
        },
        showTeacherModalDetails(teacher) {
            this.teacherModalData.name = teacher.name;
            this.teacherModalData.teach = teacher.teach;
            this.teacherModalData.image = teacher.image;
            this.teacherModalData.description = teacher.description;
        }
    },
    computed: {
        // Filter teachers with specific subject
        filteredTeachers() {
            if (!this.selectedSubject || this.selectedSubject === "") {
                return this.teachers;
            }
            return this.teachers.filter(teacher => {
                if (Array.isArray(teacher.teach)) {
                    return teacher.teach.map(subject => subject.toLowerCase()).includes(this.selectedSubject.toLowerCase());
                }
                return teacher.teach.toLowerCase() === this.selectedSubject.toLowerCase();
            });
        },
        // Generate all subjects from teachers data for filtering without duplicate
        subjects() {
            const allSubjects = this.teachers.flatMap(teacher => 
                Array.isArray(teacher.teach) ? teacher.teach : [teacher.teach]
            );
            return [...new Set(allSubjects)].sort();
        }
    }
}
</script>