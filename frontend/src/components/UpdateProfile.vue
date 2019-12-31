<template>
    <div class="container">
        <div class="row">
            <div class="col-md-6 mt-5 mx-auto">
                <form v-on:submit.prevent="updateProfile">
                    <h1 class="h3 mb-3 font-weight-normal">Update Profile</h1>
                    <div class="form-group">
                        <label for="firstName">First Name</label>
                        <input type="text" v-model="firstName" class="form-control" name="firstName" placeholder="Enter First Name">
                    </div>
                    <div class="form-group">
                        <label for="lastName">Last Name</label>
                        <input type="text" v-model="lastName" class="form-control" name="lastName" placeholder="Enter Last Name">
                    </div>
                    <div class="form-group">
                        <label for="email">Email Address</label><td>{{email}}</td>
                    </div>
                    <div class="form-group">
                        <label for="password">Password</label>
                        <input type="password" v-model="password" class="form-control" name="password" placeholder="Enter Password">
                    </div>
                    <div class="form-group">
                          <label>Upload Profile Image</label>
                            <input type="file" id="file" ref="file" @change="handleFileUpload" />
                            <button v-on:click="submitFile()">Upload</button>
                     </div>
                    <button class="btn btn-lg btn-primary btn-block">Update Profile</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import EventBus from './EventBus'
import { userService } from './_services'

export default {
  data () {
    return {
      first_name: '',
      last_name: '',
      email: '',
      password: '',
      file: ''
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
      console.log('i got triggered')
      this.file = this.$refs.file.files[0]
      console.log(event)
      this.file = event.target.files[0]
      console.log(this.file)
    },
    updateProfile () {
      // let formData = new FormData()
      // formData.append('file', this.file)
      console.log(this.file)
      userService.uploadUserProfileImage(this.file)
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
    }
  }
}

</script>
