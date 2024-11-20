# S3 Bucket
resource "aws_s3_bucket" "travel-agency-bucket" {
  bucket = "travel-agency-bucket"
}

resource "aws_s3_bucket_versioning" "travel_agency_bucket_versioning" {
  bucket = aws_s3_bucket.travel-agency-bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}