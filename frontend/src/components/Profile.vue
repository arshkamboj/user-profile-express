<template>
    <div class="container">
        <div class="jumbotron mt-5">
            <div class="col-sm-8 mx-auto">
                <h1 class="text-center">PROFILE</h1>
            </div>
            <table class="table col-md-6 mx-auto">
                <tbody>
                    <tr>
                        <td>First Name</td>
                        <td>{{firstName}}</td>
                    </tr>
                    <tr>
                        <td>Last Name</td>
                        <td>{{lastName}}</td>
                    </tr>
                    <tr>
                        <td>Email</td>
                        <td>{{email}}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import EventBus from './EventBus'
import { userService } from './_services'

export default {
  data () {
    return {
      firstName: '',
      lastName: '',
      email: ''
    }
  },
  mounted: function () {
    this.getUserProfile()
  },
  methods: {
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
