document.addEventListener("DOMContentLoaded", async () => {
  const form = document.getElementById("register-form");
  const credentialFields = document.getElementById("credential-fields");
  const metadataFields = document
    .getElementById("metadata-fields")
    .cloneNode(true);
  document.getElementById("metadata-fields").remove();
  const nextButton = document.getElementById("register-form-next");

  nextButton.addEventListener("click", () => {
    if (form.reportValidity()) {
      form.appendChild(metadataFields);
      metadataFields.hidden = false;
      credentialFields.hidden = true;
    }
  });
});
