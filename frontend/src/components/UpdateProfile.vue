<template>
    <div class="container">
        <div class="row">
            <div class="col-md-6 mt-5 mx-auto">
                <form v-on:submit.prevent="updateProfile">
                    <h1 class="h3 mb-3 font-weight-normal">Update Profile</h1>
                    <div class="form-group">
                        <label for="firstName">First Name</label>
                        <input type="text" v-model="firstName" class="form-control" name="firstName" placeholder="Enter First Name" :class="{ 'is-invalid': submitted && !firstName }" />
                        <div v-show="submitted && !firstName" class="invalid-feedback">First Name is required</div>
                    </div>
                    <div class="form-group">
                        <label for="lastName">Last Name</label>
                        <input type="text" v-model="lastName" class="form-control" name="lastName" placeholder="Enter Last Name" :class="{ 'is-invalid': submitted && !lastName }" />
                        <div v-show="submitted && !lastName" class="invalid-feedback">Last Name is required</div>
                    </div>
                    <div class="form-group">
                        <label for="email">Email Address</label><td>{{email}}</td>
                    </div>
                    <div class="form-group">
                        <label for="password">Password</label>
                        <input type="password" v-model="password" class="form-control" name="password" placeholder="Enter Password" :class="{ 'is-invalid': submitted && !password }">
                        <div v-show="submitted && !password" class="invalid-feedback">Password is required</div>
                    </div>
                    <div class="form-group">
                          <label>Upload Profile Image</label>
                            <input type="file" id="profileImage" ref="profileImage" @change="handleFileUpload" />
                            <button v-on:click="submitProfileImage()">Upload</button>
                     </div>
                    <button class="btn btn-lg btn-primary btn-block">Update Profile</button>
                    <div v-if="error" class="alert alert-danger">{{error}}</div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import EventBus from './EventBus'
import { userService } from './_services'
import axios from 'axios'
import router from '../router'

export default {
  data () {
    return {
      firstName: '',
      lastName: '',
      email: '',
      password: '',
      profileImage: '',
      returnUrl: '/profile',
      submitted: false,
      loading: false,
      error: ''
    }
  },
  mounted: function () {
    this.getUserProfile()
  },
  methods: {
    /* updateProfile () {
      axios.post('users/updateProfile', {
        first_name: this.first_name,
        last_name: this.last_name,
        email: this.email,
        password: this.password,
        formData: {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
      }).then(res => {
        router.push({ name: 'Profile' })
      }).catch(err => {
        console.log(err)
      })
    }, */
    handleFileUpload (event) {
      this.profileImage = event.target.files[0]
      console.log(this.profileImage)
    },
    submitProfileImage () {
      let formData = new FormData()
      const local = localStorage.user
      formData.append('profileImage', this.profileImage)
      console.log(this.profileImage)
      axios.post('/users/profileImage/upload', formData,
        { headers: {'Content-Type': 'multipart/form-data',
          'token': JSON.parse(local).token}
        })
        .then(
          user => {
            console.log('its a success')
          },
          error => {
            this.error = error
            this.loading = false
          }
        )
    },
    getUserProfile () {
      userService.getProfileInformation()
        .then(
          user => {
            this.firstName = user['firstName']
            this.lastName = user['lastName']
            this.email = user['email']
          },
          error => {
            this.error = error
            this.loading = false
            EventBus.$emit('')
          }
        )
    },
    updateProfile () {
      this.submitted = true
      if (!(this.firstName && this.lastName && this.password)) {
        return
      }
      this.loading = true
      console.log('hi')
      console.log(this.lastName)
      userService.updateProfile(this.firstName, this.lastName, this.email, this.password)
        .then(
          user => {
            console.log('its a success')
            router.push(this.returnUrl)
            console.log(this.returnUrl)
            console.log(user)
            // EventBus.$emit('logged-in', 'loggedin')
          },
          error => {
            this.error = error
            this.loading = false
          }
        )
    }
  }
}

</script>
