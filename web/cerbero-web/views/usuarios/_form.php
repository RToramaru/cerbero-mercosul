<?php

use yii\helpers\Html;
use yii\widgets\ActiveForm;

/** @var yii\web\View $this */
/** @var app\models\Usuarios $model */
/** @var yii\widgets\ActiveForm $form */
?>

<div class="usuarios-form card card-outline">

    <div class="card-body">
        <?php $form = ActiveForm::begin(); ?>

        <?= $form->field($model, 'nome')->textInput()->label('Digite o nome') ?>

        <?= $form->field($model, 'usuario')->textInput()->label('Digite o nome de usuário') ?>

        <?= $form->field($model, 'senha')->textInput()->label('Digite a senha') ?>

        <div class="form-group">
            <?= Html::submitButton('Salvar', ['class' => 'btn btn-success']) ?>
        </div>

        <?php ActiveForm::end(); ?>
    </div>

</div>