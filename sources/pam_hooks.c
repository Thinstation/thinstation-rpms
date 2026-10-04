#include <security/pam_appl.h>
#include <security/pam_modules.h>
#include <errno.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

static int run_hook(pam_handle_t *pamh, int argc, const char **argv,
                    const char *action)
{
    const char *user = NULL;
    char **child_argv;
    pid_t pid;
    int status;
    int rc;

    rc = pam_get_user(pamh, &user, NULL);
    if (rc != PAM_SUCCESS || user == NULL || user[0] == '\0')
        return PAM_USER_UNKNOWN;

    if (argc < 1 || argv == NULL || argv[0] == NULL || argv[0][0] == '\0')
        return PAM_SUCCESS;

    child_argv = calloc((size_t)argc + 3, sizeof(*child_argv));
    if (child_argv == NULL)
        return PAM_BUF_ERR;

    for (int i = 0; i < argc; ++i)
        child_argv[i] = (char *)argv[i];
    child_argv[argc] = (char *)action;
    child_argv[argc + 1] = (char *)user;
    child_argv[argc + 2] = NULL;

    pid = fork();
    if (pid < 0) {
        free(child_argv);
        return PAM_SESSION_ERR;
    }

    if (pid == 0) {
        execvp(child_argv[0], child_argv);
        _exit(127);
    }

    free(child_argv);

    do {
        rc = waitpid(pid, &status, 0);
    } while (rc < 0 && errno == EINTR);

    if (rc < 0)
        return PAM_SESSION_ERR;
    if (WIFEXITED(status) && WEXITSTATUS(status) == 0)
        return PAM_SUCCESS;
    return PAM_SESSION_ERR;
}

PAM_EXTERN int pam_sm_authenticate(pam_handle_t *pamh, int flags,
                                   int argc, const char **argv)
{
    const char *user = NULL;
    int rc = pam_get_user(pamh, &user, NULL);

    if (rc != PAM_SUCCESS)
        return rc;
    if (user == NULL || user[0] == '\0') {
        rc = pam_set_item(pamh, PAM_USER, "nobody");
        if (rc != PAM_SUCCESS)
            return PAM_USER_UNKNOWN;
    }
    return PAM_SUCCESS;
}

PAM_EXTERN int pam_sm_setcred(pam_handle_t *pamh, int flags,
                              int argc, const char **argv)
{
    return PAM_SUCCESS;
}

PAM_EXTERN int pam_sm_acct_mgmt(pam_handle_t *pamh, int flags,
                                int argc, const char **argv)
{
    return PAM_SUCCESS;
}

PAM_EXTERN int pam_sm_chauthtok(pam_handle_t *pamh, int flags,
                                int argc, const char **argv)
{
    return PAM_SUCCESS;
}

PAM_EXTERN int pam_sm_open_session(pam_handle_t *pamh, int flags,
                                   int argc, const char **argv)
{
    return run_hook(pamh, argc, argv, "open");
}

PAM_EXTERN int pam_sm_close_session(pam_handle_t *pamh, int flags,
                                    int argc, const char **argv)
{
    return run_hook(pamh, argc, argv, "close");
}
