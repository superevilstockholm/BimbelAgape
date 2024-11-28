<template>
    <!-- Hero Section -->
    <section class="px-0 mx-0 text-light">
        <div class="container-fluid mx-0 px-0">
            <div class="position-relative p-0 m-0" style="height: 700px !important;">
                <img class="position-absolute z-1" style="width: 100%; max-width: 100%; height: 100%; object-fit: cover; object-position: top; filter: brightness(50%) contrast(105%); image-rendering: crisp-edges; pointer-events: none;" src="@/assets/teachers_main_section1.jpg" alt="">
                <div class="position-absolute z-3 w-100 h-100" style="background-color: rgba(0, 0, 0, 0.17);">
                    <div class="container w-100 h-100 py-0 my-0">
                        <div class="row w-100 h-100 p-0 m-0">
                            <div class="d-flex flex-c   olumn w-100 h-100 align-items-center justify-content-center p-0 m-0">
                                <div class="d-flex flex-column w-100 p-0 m-0 align-items-center" style="animation: slideUpTextAnimation 2s ease;">
                                    <h1 class="fw-bold text-center pb-0 mb-0 hero-section-title-responsive" style="font-family: 'Inter', Helvetica, sans-serif, serif;">Teachers And Staff</h1>
                                    <p class="text-center hero-section-description-responsive">Our dedicated teachers and staff are the backbone of our educational community. With a passion for teaching and a commitment to excellence, they work tirelessly to inspire and guide students toward achieving their full potential. Get to know the talented professionals who shape our learning environment.</p>
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
    <section class="py-5 my-5">
        <div class="container">
            <h1 class="text-center mb-5 fw-medium" style="font-family: 'opsz', 'Inter', Helvetica, sans-serif, serif; font-size: 3.5rem;">Meet Our Teachers</h1>
            <div class="d-flex justify-content-center mb-4">
                <select v-model="selectedSubject" class="form-select w-50">
                    <option value="">All Subjects</option>
                    <option v-for="subject in subjects" :value="subject" :key="subject">{{ subject }}</option>
                </select>
            </div>
            <!-- Modal -->
            <div class="modal" id="teacherDetailsModal" tabindex="-1" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">Modal title</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <ul style="list-style: none;">
                                <li v-for="(value, key, index) in tacherModalData" v-bind:key="index">
                                    <div class="row d-flex flex-row align-items-center">
                                        <div class="col-5">
                                            {{ key }}
                                        </div>
                                        <div class="col-2"> : </div>
                                        <div class="col-5">
                                            {{ value }}
                                        </div>
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
                        <img :src="teacher.image" class="card-img-top border-0 p-0 m-0" style="filter: brightness(80%)" alt="Teacher 1">
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
</template>
<style>
@import url('https://fonts.googleapis.com/?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');

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
.card {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.card:hover {
    transform: scale(1.05);
    box-shadow: 0 0 10px 20px rgba(0, 0, 0, 0.5);
}
.card {
    animation: opacityCardAnimation 0.6s ease-out forwards;
    animation-timeline: view(block 120% 0%);
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
@keyframes opacityCardAnimation {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}
</style>
<script>
export default {
    data() {
        return {
            heroSectionBackgroundImages: ['teachers_main_section.jpeg', 'teachers_main_section1.jpg'],
            teachers: [
                {
                    'name': 'Ruth Natalia Pangaribuan',
                    'teach': ['Math'],
                    'image': '/assets/ruth_natalia.jpg',
                    'description': 'Ruth is a passionate and experienced Math teacher, known for her engaging approach to teaching. She helps students grasp complex mathematical concepts with ease and enthusiasm.'
                },
                {
                    'name': 'Aprila Safira Eka Rani',
                    'teach': ['English', 'Piano'],
                    'image': '/assets/safira.jpg',
                    'description': 'Aprila brings a unique combination of English language teaching and piano instruction. Her creativity and passion for both fields inspire students to develop strong language skills and musical talents.'
                },
                {
                    'name': 'Fitri Utari',
                    'teach': ['Math', 'English'],
                    'image': '/assets/fitri.jpg',
                    'description': 'Fitri is a dedicated teacher who specializes in both Math and English. Her ability to simplify complex topics helps students succeed in these essential subjects.'
                },
                {
                    'name': 'Wulan',
                    'teach': ['English'],
                    'image': '/assets/wulan.jpeg',
                    'description': 'Wulan is an expert in English education, focusing on building strong communication skills. She makes learning English both fun and effective.'
                },
                {
                    'name': 'Leo Sin Pandi',
                    'teach': ['Calistung'],
                    'image': '/assets/pandi.jpg',
                    'description': 'Leo specializes in early childhood education, focusing on Calistung (early literacy and numeracy). He helps young learners develop a strong foundation for their academic journey.'
                },
                {
                    'name': 'Erwin Setiawan',
                    'teach': ['Computer'],
                    'image': '/assets/erwin.jpg',
                    'description': 'Erwin is a tech-savvy educator who teaches Computer Science. He inspires students to embrace technology and equips them with the skills needed for the digital world.'
                },
                {
                    'name': 'Grace Herliana',
                    'teach': ['Piano'],
                    'image': '/assets/unknown.png',
                    'description': 'Grace is a talented Piano teacher who nurtures her students’ musical abilities. Her lessons emphasize both technical skill and artistic expression in music.'
                },
                {
                    'name': 'Ombilin Hutabarat',
                    'teach': ['Football'],
                    'image': '/assets/billy.jpg',
                    'description': 'Ombilin is a passionate football coach who teaches teamwork, discipline, and athleticism. His lessons not only focus on the sport but also on life skills that help students grow both on and off the field.'
                },
                {
                    'name': 'Hisar Martha Ganda Situmorang',
                    'teach': ['Korea'],
                    'image': '/assets/unknown.png',
                    'description': 'Hisar is a Korean language expert who introduces students to the beauty of the Korean culture and language. Her lessons are interactive and fun, making it easy for students to learn.'
                },
                {
                    'name': 'Ramanda',
                    'teach': ['Staff Library'],
                    'image': '/assets/unknown.png',
                    'description': 'Ramanda plays an essential role in managing the school library. He ensures that students have access to a wide range of resources and creates a welcoming space for reading and learning.'
                }
            ],
            selectedSubject: "",
            tacherModalData: {
                'name': null,
                'teach': null,
                'image': null,
                'description': null,
                'gender': 'female',
                'age': 18,
                'experience': 4,
                'quote': 'the quieter you become, the more you are able to hear'
            }
        }
    },
    methods: {
        showTeacherModalDetails(teacher) {
            this.tacherModalData.name = teacher.name;
            this.tacherModalData.teach = teacher.teach;
            this.tacherModalData.image = teacher.image;
            this.tacherModalData.description = teacher.description;
        }
    },
    computed: {
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
        subjects() {
            const allSubjects = this.teachers.flatMap(teacher => 
                Array.isArray(teacher.teach) ? teacher.teach : [teacher.teach]
            );
            return [...new Set(allSubjects)].sort();
        }
    }
}
</script>